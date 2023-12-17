'''
Module defining auxiliary ManagerResult
'''

from dataclasses import dataclass


@dataclass
class ManagerResult:
    '''
    Dataclass for managers' return values
    '''
    succeed: bool
    message: str
    result:  any = None
