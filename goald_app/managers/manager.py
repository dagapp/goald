'''
Module defining auxiliary AuthManager and ManagerResult
'''

from dataclasses import dataclass
from django.db.models.manager import Manager


@dataclass
class ManagerResult:
    '''
    Dataclass for managers' return values
    '''
    succeed: bool
    message: str
    result:  Manager = None


class AuthManager:
    '''
    Parent class for managers that require user auth
    '''
    user_id: int = None

    @staticmethod
    def auth(user_id: int):
        '''
        Auth a user with given id
        '''
        AuthManager.user_id = user_id
