'''
Module for handling group records in table
'''

from goald_app.managers.manager import ManagerResult
from goald_app.models import Group


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
    def create(tag, is_public, name, leader_id) -> ManagerResult:
        Group.objects.create(tag=tag, is_public=is_public, name=name, leader_id=leader_id)