"""List of ids of available session (i.e. simulated conversation) in database"""
from typing import List

from api.data_for_simulation.db_conv import DB_CONV
from api.common.data_models import ChatSessionInfo


def get_sessions_info() -> List[ChatSessionInfo]:
    """Get all chat sessions and associated infos"""
    sessions:List[ChatSessionInfo] = []
    for chat_session in DB_CONV:
        chat_session_info = ChatSessionInfo(
            session_id=chat_session.session_id,
            nb_messages=len(chat_session.conversation)
        )
        sessions.append(chat_session_info)
    return sessions
