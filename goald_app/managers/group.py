from .manager import ManagerResult
from ..models import Group
from ..models import User
from bcrypt import gensalt, hashpw

import string 
import random

class GroupManager():
    '''
    Manager to handle groups in table
    '''
    @staticmethod
    def objects_all() -> ManagerResult:
        '''
        Get all groups from table
        '''
        return ManagerResult(True, "", Group.objects.all())

    @staticmethod
    def objects_get(group_id: int) -> ManagerResult:
        '''
        Get a group with given name from the table
        '''
        try:
            return ManagerResult(True, "Group found", Group.objects.get(id=group_id))
        except Group.DoesNotExist:
             return ManagerResult(False, "Group doesnt exist!")
        
    @staticmethod
    def exists(id: int) -> ManagerResult:
        if Group.objects.filter(id=id).exists():
                return ManagerResult(True, "Group exists")

        return ManagerResult(False, "Group doesnt exist!")

    @staticmethod
    def create(leader_id: int, name: str, image: str = "static/images/groupProfiles/group_pic.png", is_public: bool = True) -> ManagerResult:
        if Group.objects.filter(name=name).exists():
            return ManagerResult(False, "Group already exists!")
        
        tag = '@' + ''.join(name_ch if name_ch in string.ascii_letters or name_ch in string.digits else '_' for name_ch in name)
        while Group.object.get(tag=tag).exists(): tag += random.choice(string.digits)

        Group.objects.create(leader_id=User.objects.get(id=leader_id), name=name, tag=tag, image=image, is_public=is_public)

        return ManagerResult(True, "Group created successfully!")
    
