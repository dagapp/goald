"""
Module defining auxiliary ManagerResult
"""

from dataclasses import dataclass


class DoesNotExist(Exception):
    pass

class AlreadyExists(Exception):
    pass

class IncorrectData(Exception):
    pass
