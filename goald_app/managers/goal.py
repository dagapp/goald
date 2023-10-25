from bcrypt import gensalt, hashpw

from .manager import ManagerResult, AuthManager
from .user import UserManager
from ..models import User, Group, Goal

class GoalManager():
    @staticmethod
    def objects_all() -> ManagerResult:
        try:
            result = []
            groups = Group.objects.filter(users__id=AuthManager.user_id)
            for group in groups:
                result += Goal.objects.filter(group_id=group)
                
            if result:
                return ManagerResult(True, "", result)
            
        except Goal.DoesNotExist:
            pass
        
        return ManagerResult(False, "No goals found!")

    @staticmethod
    def objects_get(id: int) -> ManagerResult:
        try:
            users = User.objects.filter(id=AuthManager.user_id, groups__id=Group.objects.filter(goal__id=id)[0].id)
            if users:
                result = Goal.objects.filter(id=id)
                return ManagerResult(True, "", result)
            
        except Goal.DoesNotExist:
            pass
        
        return ManagerResult(False, "No goal found!")