'''
Module for handling group records in db
'''

import string
import random

from goald_app.models import Group
from goald_app.models import User

from goald_app.managers.manager import ManagerResult


class GroupManager:
    '''
    Manager for handling groups in table
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
    def exists(group_id: int) -> ManagerResult:
        '''
        Check if group exists
        '''
        if Group.objects.filter(id=group_id).exists():
            return ManagerResult(True, "Group exists")

        return ManagerResult(False, "Group doesnt exist!")

    @staticmethod
    def create(
        leader_id: int,
        name: str,
        image: str,
        is_public: bool = True,
    ) -> ManagerResult:
        '''
        Create a group with given leader_id, name, image and is_public arguments
        '''
        if Group.objects.filter(name=name).exists():
            return ManagerResult(False, "Group already exists!")

        tag = "@" + "".join(
            name_ch
            if name_ch in string.ascii_letters or name_ch in string.digits
            else "_"
            for name_ch in name
        )
        while Group.objects.filter(tag=tag).exists():
            tag += random.choice(string.digits)

        Group.objects.create(
            leader_id=User.objects.get(id=leader_id),
            name=name,
            tag=tag,
            image=image,
            is_public=is_public,
        )

        return ManagerResult(True, "Group created successfully!")
