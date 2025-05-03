"""List of ids of available session (i.e. simulated conversation) in database"""
from typing import List

from api.data.db_conv import DB_CONV


def get_session_ids() -> List[int]:
    """
    Get all session ids
    """
    return [db_object.session_id for db_object in DB_CONV]
