"""App data models"""
from enum import StrEnum

from pydantic import BaseModel
from typing import List, Optional

from api.common.constants import DEFAULT_TIMESTAMP

class UserType(StrEnum):
    ASSISTANT = "Assistant"
    EMPLOYEE = "Employee"
    CUSTOMER = "Customer"
    NA = "na"


class User(BaseModel):
    user_id: int
    user_type: UserType
    user_name: str


class ChatSessionInfo(BaseModel):
    session_id: int
    nb_messages: int


class UserMessage(BaseModel):
    user_id: int
    user_type: Optional[UserType] = UserType.NA
    user_name: Optional[str] = ""
    timestamp: Optional[float] = DEFAULT_TIMESTAMP
    message: str
    nb_tokens: Optional[int] = 0


class ChatPayloadAndDbObject(BaseModel):
    session_id: int
    conversation: List[UserMessage]


class MessageRetrievalInputPayload(BaseModel):
    session_id: int
    message_id: int


class ContextUnit(BaseModel):
    role: str
    content: str
