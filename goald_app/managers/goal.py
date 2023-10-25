from bcrypt import gensalt, hashpw

from .manager import ManagerResult, AuthManager
from ..models import Goal

class GoalManager(AuthManager):
    @staticmethod
    def objects_get(id=id) -> ManagerResult:
        try:
            return ManagerResult(True, "", Goal.objects.get(id=id))
        except Goal.DoesNotExist:
            return ManagerResult(False, "Goal doesnt exist!")