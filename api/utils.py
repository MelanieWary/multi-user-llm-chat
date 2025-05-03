"""Utils for multi-user chat"""
from typing import Dict, List, Optional

from api.common.prompts import ASSISTANT_REMINDER_PROMPT
from api.common.data_models import ContextUnit, ChatPayloadAndDbObject, UserMessage, UserType


def make_conversation_from_payload(payload: ChatPayloadAndDbObject) -> str:
    conv = ""
    for user_message in payload.conversation:
        if conv != "":
            conv += "\n"
        conv += f"[{user_message.user_type} (name: {user_message.user_name})] {user_message.message}"
    return conv


def make_context_from_payload(
        payload: ChatPayloadAndDbObject,
        reminder: Optional[Dict] = ASSISTANT_REMINDER_PROMPT
) -> List[ContextUnit]:
    conv = make_conversation_from_payload(payload)
    context = [
        ContextUnit(
            role="user",
            content=conv,
        ),
        reminder,
    ]
    return context


def append_message_to_payload(input_payload: ChatPayloadAndDbObject, user_message: UserMessage):
    """
    Add llm response (or new message) to conv
    """
    if not (user_message.user_type == UserType.ASSISTANT and user_message.message == 'Nothing relevant'):
        input_payload.conversation.append(user_message)
    else:
        pass
