from dataclasses import dataclass

# Dataclass for managers' return values
@dataclass
class ManagerResult:
    succeed: bool
    message: str
    result:  object = None

# Parent class for managers that require user auth
class AuthManager:
    user_id: int = None

    @staticmethod
    def auth(user_id: int):
        user_id = user_id
