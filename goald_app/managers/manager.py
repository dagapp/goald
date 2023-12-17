'''
Module defining auxiliary ManagerResult
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
    result:  any = None
