"""
Module for handling group records in db
"""

import string
import random

from goald_app.models import Group
from goald_app.models import User

from goald_app.managers.common import DoesNotExist, AlreadyExists


class GroupManager:
    """
    Manager for handling groups in table
    """

    @staticmethod
    def get_all() -> any:
        """
        Get all groups from table
        """
        return Group.objects.all()

    @staticmethod
    def get(group_id: int) -> any:
        """
        Get a group with given name from the table
        """
        try:
            return Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def get_all_by_user_id(user_id: int) -> any:
        """
        Get all groups by given user_id
        """
        try:
            return Group.objects.filter(users__id=user_id)
        except Group.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def exists(group_id: int) -> bool:
        """
        Check if group exists
        """
        return Group.objects.filter(id=group_id).exists()

    @staticmethod
    def create(
        name: str,
        image: str,
        leader_id: int,
        password: str = None,
        is_public: bool = True,
    ) -> None:
        """
        Create a group with given leader_id, name, image and is_public arguments
        """
        if Group.objects.filter(name=name).exists():
            raise AlreadyExists

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
            raise DoesNotExist

    @staticmethod
    def add_user(group_id: int, login: int) -> None:
        """
        Add user to a group
        """
        try:
            try:
                Group.objects.get(id=group_id).users.add(User.objects.get(login=login))
            except User.DoesNotExist:
                raise DoesNotExist
        except Group.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def del_user(group_id: int, user_id: int) -> None:
        """
        Delete user from a group
        """
        try:
            Group.objects.get(id=group_id).users.get(id=user_id).delete()
        except Group.DoesNotExist:
            raise DoesNotExist
