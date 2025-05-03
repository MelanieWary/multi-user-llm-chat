"""Hardcoded users  database for chat simulation"""
from typing import List

from api.common.constants import EMPLOYEE_NAME
from api.common.data_models import User, UserType


DB_USERS: List[User] = [
    User(
        user_id=1,
        user_type=UserType.EMPLOYEE,
        user_name=EMPLOYEE_NAME,
    ),
    User(
        user_id=2,
        user_type=UserType.CUSTOMER,
        user_name="Melinda Roberts",
    ),
    User(
        user_id=3,
        user_type=UserType.CUSTOMER,
        user_name="Jason Lopez",
    ),
    User(
        user_id=4,
        user_type=UserType.CUSTOMER,
        user_name="Mario Smith",
    ),
    User(
        user_id=5,
        user_type=UserType.CUSTOMER,
        user_name="John Murray",
    ),
    User(
        user_id=6,
        user_type=UserType.CUSTOMER,
        user_name="Ana Johnson",
    ),
    User(
        user_id=7,
        user_type=UserType.CUSTOMER,
        user_name="Megan Doe",
    ),
    User(
        user_id=8,
        user_type=UserType.CUSTOMER,
        user_name="John Bell",
    ),
    User(
        user_id=9,
        user_type=UserType.CUSTOMER,
        user_name="Amanda Laurens",
    ),
    User(
        user_id=10,
        user_type=UserType.CUSTOMER,
        user_name="Brian Memphis",
    ),
]