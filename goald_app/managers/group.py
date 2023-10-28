from .manager import ManagerResult
from ..models import Group

class GroupManager():
    @staticmethod
    def objects_all() -> ManagerResult:
        return ManagerResult(True, "", Group.objects.all())
    
    @staticmethod
    def objects_get(name: str) -> ManagerResult:
        try:
            return ManagerResult(True, "User found", Group.objects.get(name=name))
        except Group.DoesNotExist:
             return ManagerResult(False, "User doesnt exist!")