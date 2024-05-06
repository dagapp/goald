"""
Runtime exceptions definition file
"""


class DoesNotExist(Exception):
    """
    Exception for handling events of non-existent rows
    """


class AlreadyExists(Exception):
    """
    Exception for handling events of already existent rows
    """


class IncorrectData(Exception):
    """
    Exception for handling events of incorrect data given
    """
