"""Retrieve the nth message of the chat session, and call the LLM with it + selected chat history"""

from api.common.data_models import MessageRetrievalInputPayload, ChatPayloadAndDbObject, UserMessage, UserType
from api.data_for_simulation.db_conv import DB_CONV
from api.data_for_simulation.db_users import DB_USERS

# Option 1 - prepare for a non simulated chat
# (input payload = last message (retrieved previously by through another endpoint))
# init a working_db (that we would use here in a non-simulated chat) ??
# extract_required_message from DB_CONV
# retrieve and select chat history from working_db
# add required_message to working_db (with nb_tokens and timestamp)
# and common : build context, call llm, build output

# Option 2 - fully simulated without preparation for future non simulated
# use only DB_CONV
# retrieve_full_history
# from full history: extract_history_up_to_required_message
# from extracted history: extract_required_message (+ replace its timestamp and nb_tokens)
# and common : build context, call llm, build output


def retrieve_full_history(session_id, message_id, db):
    #db = DB_CONV when used to get the required message
    #db = working_db when used to get the selected history for context
    pass

# OR
def extract_history_up_to_required_message(session_id, message_id, db):
    pass

def extract_required_message(history_up_to_required_message):
    """incl: set its timestamp and save it in working DB"""
    pass

def retrieve_selected_history(history_up_to_required_message):
    """
    from working DB
    return history + required message
    incl : computation of nb_tokens (of required message)+ save it in DB
    """
    pass

def call_llm(selected_history, reminder_prompt):
    pass

def build_output_payload(required_message, llm_response, DB_USERS):
    """include"""
    pass


def get_next_user_and_assistant_messages(payload: MessageRetrievalInputPayload) -> ChatPayloadAndDbObject:
    # retrieve the nth message of the chat session,
    # retrieve the selected chat history
    # call the llm
    # build payload : nth message + llm response if relevant, with all user details
    # (user_id, type, name) and message details (timestamp, message)

    return ChatPayloadAndDbObject(
        session_id=payload.session_id,
        conversation=[
            UserMessage(
                user_id=2,
                user_type=UserType.CUSTOMER,
                user_name="Testeur TESTEUR",
                timestamp=0.0,
                message="Ceci est un test"
            ),
        ]
    )

def get_assistant_response(payload: ChatPayloadAndDbObject):
    return ChatPayloadAndDbObject(
        session_id=payload.session_id,
        conversation=[
            UserMessage(
                user_id=0,
                user_type=UserType.ASSISTANT,
                user_name="Bob",
                timestamp=0.0,
                message="Ceci est un test, des fois il n'aura rien à dire"
            ),
        ]
    )