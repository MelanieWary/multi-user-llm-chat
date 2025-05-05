"""Call the LLM with last message sent in chat session + relevant chat history"""
from loguru import logger
from typing import Dict, List, Optional, Tuple

from api.common.constants import ASSISTANT_NAME, DEFAULT_LLM_RESPONSE, EMPLOYEE_NAME
from api.common.data_models import (
    ChatPayloadAndDbObject,
    ContextUnit,
    UserMessage,
    UserType
)
from api.common.prompts import ASSISTANT_SYSTEM_PROMPT, ASSISTANT_REMINDER_PROMPT
from api.common.utils import get_timestamp, get_customer_name
from api.llm_utils.openai_llm import ENCODING, query_llm
from config import DURATION_MAX, MESSAGES_MAX, TOKENS_MAX


# initialzing DB
working_db_conv = {}  # TODO: replace with "real" DB


def get_nb_tokens(message:UserMessage) -> int:
    """
    Assess the number of tokens of a message.
    15 = nb of tokens of extra elements added to the message when building the context
    """
    text = f"[{message.user_type} (name: {message.user_name})] {message.message}"
    return len(ENCODING.encode(text)) + 15


def update_history(session_id:int, message:UserMessage, database):
    """
    Add message to the chat session history (with its nb_tokens estimated)
    """
    history = database.setdefault(session_id, [])
    message.nb_tokens = get_nb_tokens(message)
    logger.info(f"Adding new message to the chat session history {session_id}")
    history.append(message)
    database[session_id] = history


def get_history(
        session_id: int,
        database,
        duration_max: int,
        tokens_max: int,
        messages_max: int
) -> Tuple[bool, List[UserMessage]]:
    """
    Retrieve conversation history that is :
    * <= <duration_max> seconds old
    * or <= <tokens_max> tokens long
    * or <= <messages_max> messages long

    To come: use RAG to also include older messages that are the most relevant regarding last message
    ---> all messages in vectorial DB -> retrieve those relevant (i.e. those above a TBD similarity threshold)
    and add them to at start of returned history)
    """
    full_history = database.get(session_id, [])

    #Check if there is already a message from the LLM
    first_assistant_message = not any([e for e in full_history if e.user_type == UserType.ASSISTANT])

    # Select history
    timestamp = get_timestamp()
    tot_tokens = 0
    tot_messages = 0
    history = []
    logger.info("Retrieving chat session history")
    for user_message in reversed(full_history):
        timestamp_diff = timestamp - user_message.timestamp
        tot_tokens += user_message.nb_tokens
        tot_messages += 1
        if timestamp_diff < duration_max and tot_tokens < tokens_max and tot_messages < messages_max:
            history.append(user_message)
        else:
            break
    history.reverse()
    return first_assistant_message, history


def make_conversation_from_history(history: List[UserMessage]) -> str:
    """
    Make a dialog-like conversation from history
    """
    conv = ""
    for user_message in history:
        if conv != "":
            conv += "\n"
        conv += f"[{user_message.user_type} (name: {user_message.user_name})] {user_message.message}"
    return conv


def make_context_from_history(
    history: List[UserMessage],
    reminder: Optional[Dict] = ASSISTANT_REMINDER_PROMPT
) -> List[ContextUnit]:
    """Build the context to pass to the LLM from chat session history"""
    conv = make_conversation_from_history(history)
    logger.info(f"--------- Selected history: {conv}")  #TODO to delete
    context = [
        ContextUnit(
            role="user",
            content=conv,
        ),
        reminder,
    ]
    return context


def get_assistant_response(payload: ChatPayloadAndDbObject):
    """Return assistant (LLM) response to a chat session message"""
    session_id = payload.session_id
    message = payload.conversation[0]

    update_history(
        session_id=session_id,
        message=message,
        database=working_db_conv,
    )

    first_assistant_message, history = get_history(
        session_id=session_id,
        database=working_db_conv,
        duration_max=DURATION_MAX,
        tokens_max=TOKENS_MAX,
        messages_max=MESSAGES_MAX,
    )

    context = make_context_from_history(
        history=history,
        reminder=ASSISTANT_REMINDER_PROMPT
    )

    try:
        response = query_llm(
            system_prompt=ASSISTANT_SYSTEM_PROMPT,
            context=context,
        )
        assistant_response = response.output_text

        if not assistant_response == '(nothing relevant)':
            if first_assistant_message:  # That would be its first message sent to the chat session
                customer_name = get_customer_name(session_id=session_id)
                assistant_response = f"Hello {customer_name}, hi {EMPLOYEE_NAME}. {assistant_response}"

            assistant_message = UserMessage(
                user_type=UserType.ASSISTANT,
                user_name=ASSISTANT_NAME,
                user_id=0,
                timestamp=get_timestamp(),
                message=assistant_response,
            )

            update_history(
                session_id=session_id,
                message=assistant_message,
                database=working_db_conv)

        else:
            assistant_message = UserMessage(
                user_type=UserType.ASSISTANT,
                user_name=ASSISTANT_NAME,
                user_id=0,
                timestamp=get_timestamp(),
                message=DEFAULT_LLM_RESPONSE,
            )

    except Exception:
        assistant_message = UserMessage(
            user_type=UserType.ASSISTANT,
            user_name=ASSISTANT_NAME,
            user_id=0,
            timestamp=get_timestamp(),
            message="NOT TO DISPLAY -- issue with LLM",
        )

    output_payload = ChatPayloadAndDbObject(
        session_id=session_id,
        conversation=[assistant_message]
    )

    return output_payload
