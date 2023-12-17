'''
Module for handling group records in db
'''

import string
import random

from goald_app.models import Group
from goald_app.models import User

from goald_app.managers.common import ManagerResult


class GroupManager:
    '''
    Manager for handling groups in table
    '''

    @staticmethod
    def get_all() -> ManagerResult:
        '''
        Get all groups from the table
        '''
        return ManagerResult(True, "", Group.objects.all())

    @staticmethod
    def get(group_id: int) -> ManagerResult:
        '''
        Get a group with given name from the table
        '''
        try:
            return ManagerResult(True, "Group found", Group.objects.get(id=group_id))
        except Group.DoesNotExist:
            pass

        return ManagerResult(False, "Group doesnt exist!")

    @staticmethod
    def get_all_by_user_id(user_id: int) -> ManagerResult:
        '''
        Get all groups by given user_id
        '''
        try:
            return ManagerResult(
                True, "Groups found", Group.objects.filter(users__id=user_id)
            )
        except Group.DoesNotExist:
            pass

        return ManagerResult(False, "No groups found!")

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
        name: str,
        image: str,
        leader_id: int,
        password: str = None,
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

        group = Group.objects.create(
            tag=tag,
            is_public=is_public,
            name=name,
            password=password,
            image=image,
            leader=User.objects.get(id=leader_id),
        )

        try:
            group.users.add(User.objects.get(id=leader_id))
        except User.DoesNotExist:
            return ManagerResult(False, "User doesn't exist!")

        return ManagerResult(True, "Group created successfully!")

    @staticmethod
    def add_user(group_id: int, user_id: int) -> ManagerResult:
        '''
        Add user to a group
        '''
        try:
            try:
                Group.objects.get(id=group_id).users.add(User.objects.get(id=user_id))
            except User.DoesNotExist:
                return ManagerResult(False, "User doesn't exist!")
        except Group.DoesNotExist:
            pass

        return ManagerResult(False, "Group doesn't exist!")

    @staticmethod
    def del_user(group_id: int, user_id: int) -> ManagerResult:
        '''
        Delete user from a group
        '''
        try:
            Group.objects.get(id=group_id).users.get(id=user_id).delete()
        except Group.DoesNotExist:
            pass

        return ManagerResult(False, "Group doesn't exist!")
