from .manager import ManagerResult
from ..models import Group
from ..models import User
from bcrypt import gensalt, hashpw

#from django.views.generic.detail import DetailView

class GroupManager():
    @staticmethod
    def objects_all() -> ManagerResult:
        return ManagerResult(True, "", Group.objects.all())
    
    @staticmethod
    def objects_get(group_id) -> ManagerResult:
        try:
            return ManagerResult(True, "Group found", Group.objects.get(id=group_id))
        except Group.DoesNotExist:
             return ManagerResult(False, "User doesnt exist!")
        
    @staticmethod
    def exists(id: int) -> ManagerResult:
        if Group.objects.filter(id=id).exists():
                return ManagerResult(True, "Group exists")

        return ManagerResult(False, "Group doesnt exist!")
    
    @staticmethod
    def create(leader_id : int, tag: str, image: str, is_public: bool) -> ManagerResult:
        if Group.objects.filter(tag=tag).exists():
            return ManagerResult(False, "Group already exists!")
        
        Group.objects.create(leader_id = User.objects.get(id = leader_id),tag=tag, image=image, is_public=is_public)

        return ManagerResult(True, "Group created successfully!")