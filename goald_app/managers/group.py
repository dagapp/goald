from .manager import ManagerResult
from ..models import Group
from ..models import User
from bcrypt import gensalt, hashpw

import string 
import random

class GroupManager():
    @staticmethod
    def objects_all() -> ManagerResult:
        return ManagerResult(True, "", Group.objects.all())
    
    @staticmethod
    def objects_get(id: int) -> ManagerResult:
        try:
            return ManagerResult(True, "Group found", Group.objects.get(id=id))
        except Group.DoesNotExist:
             return ManagerResult(False, "Group doesnt exist!")
        
    @staticmethod
    def exists(id: int) -> ManagerResult:
        if Group.objects.filter(id=id).exists():
                return ManagerResult(True, "Group exists")

        return ManagerResult(False, "Group doesnt exist!")

    @staticmethod
    def create(leader_id: int, name: str, image: str, is_public: bool) -> ManagerResult:
        if Group.objects.filter(name=name).exists():
            return ManagerResult(False, "Group already exists!")
        
        tag = "@" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))

        Group.objects.create(leader_id=User.objects.get(id = leader_id), name=name, tag=tag, image=image, is_public=is_public)

        return ManagerResult(True, "Group created successfully!")
    
