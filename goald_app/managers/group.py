from .manager import ManagerResult
from ..models import Group

class GroupManager():
    @staticmethod
    def objects_all() -> ManagerResult:
        return ManagerResult(True, "", Group.objects.all())
    
    @staticmethod
    def objects_get(group_id) -> ManagerResult:
        try:
            return ManagerResult(True, "Group found", Group.objects.get(id=group_id))
        except Group.DoesNotExist:
             return ManagerResult(False, "Group doesnt exist!")
        
    @staticmethod
    def create(tag, is_public, name, leader_id) -> ManagerResult:
        Group.objects.create(tag=tag, is_public=is_public, name=name, leader_id=leader_id)