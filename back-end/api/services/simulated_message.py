"""
Now: retrieve simulated message (from employee and customer) from DB
Future ?: Call LLM to simulate customer answer
"""

from api.common.data_models import ChatPayloadAndDbObject, UserMessage, UserType
from api.common.utils import get_timestamp, get_user_details
from api.data_for_simulation.db_conv import DB_CONV


def get_mocked_message(session_id: int, message_id: int) -> ChatPayloadAndDbObject:
    """Return the requested mocked message"""
    chat_session = [e for e in DB_CONV if e.session_id == session_id][0]
    message = chat_session.conversation[message_id]
    user_details = get_user_details(message.user_id)
    return ChatPayloadAndDbObject(
        session_id=session_id,
        conversation=[
            UserMessage(
                user_id=message.user_id,
                user_type=user_details.user_type,
                user_name=user_details.user_name,
                timestamp=get_timestamp(),
                message=message.message,
            ),
        ]
    )
