"""
Module defining auxiliary ManagerResult
"""


class DoesNotExist(Exception):
    """
    Exception for handling events of non-existent rows
    """
    pass

class AlreadyExists(Exception):
    """
    Exception for handling events of already existent rows
    """
    pass

class IncorrectData(Exception):
    """
    Exception for handling events of incorrect data given
    """
    pass
