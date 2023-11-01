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
    def objects_get(name: str) -> ManagerResult:
        '''
        Get a group with given name from the table
        '''
        try:
            return ManagerResult(True, "User found", Group.objects.get(name=name))
        except Group.DoesNotExist:
            return ManagerResult(False, "User doesnt exist!")
