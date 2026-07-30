from enum import Enum


class UserType(str, Enum):
    ARNAB = "arnab"
    TAMASA = "tamasa"


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"