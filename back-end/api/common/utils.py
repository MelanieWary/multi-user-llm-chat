"""App utils"""
from datetime import datetime

from api.common.data_models import User
from api.data_for_simulation.db_conv import DB_CONV
from api.data_for_simulation.db_users import DB_USERS


def get_user_details(user_id:int) -> User:
    """Return user details (tupe and name) from user_id"""
    return [e for e in DB_USERS if e.user_id == user_id][0]


def get_customer_name(session_id:int) -> str:
    # get users from DB_CONV  # TODO: to be improved
    chat_session = [e for e in DB_CONV if e.session_id == session_id][0]
    customer_id = [
        user_message.user_id for user_message in chat_session.conversation
        if (user_message.user_id != 0 and user_message.user_id != 1)
    ][0]
    # get the customer one
    user_details = get_user_details(user_id=customer_id)
    return user_details.user_name


def get_timestamp():
    return datetime.timestamp(datetime.now())
