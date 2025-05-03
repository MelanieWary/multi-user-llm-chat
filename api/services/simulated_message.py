"""
Now: retrieve simulated message (from employee and customer) from DB
Future ?: Call LLM to simulate customer answer
"""
from datetime import datetime

from api.common.data_models import ChatPayloadAndDbObject, UserMessage, UserType
from api.data_for_simulation.db_conv import DB_CONV
from api.data_for_simulation.db_users import DB_USERS


def get_mocked_message(session_id: int, message_id: int) -> ChatPayloadAndDbObject:
    chat_session = [e for e in DB_CONV if e.session_id == session_id][0]
    message = chat_session.conversation[message_id]
    user_details = [e for e in DB_USERS if e.user_id == message.user_id][0]
    return ChatPayloadAndDbObject(
        session_id=session_id,
        conversation=[
            UserMessage(
                user_id=message.user_id,
                user_type=user_details.user_type,
                user_name=user_details.user_name,
                timestamp=datetime.timestamp(datetime.now()),
                message=message.message,
            ),
        ]
    )
