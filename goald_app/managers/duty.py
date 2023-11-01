'''
Module for handling duty records in table
'''

from goald_app.managers.manager import ManagerResult
from goald_app.models import Duty


class DutyManager():
    '''
    Manager to handle duties in table
    '''
    @staticmethod
    def objects_all() -> list:
        '''
        Get all duties from the table
        '''
        return Duty.objects.all()

    @staticmethod
    def create(user_id: int, goal_id: int, goal: int) -> ManagerResult:
        '''
        Create a duty with given user_id, goal_id, final_value
        '''
        if Duty.objects.filter(user_id=user_id, goal_id=goal_id).exists():
            return ManagerResult(False, "Duty already exists!")

        Duty.objects.create(user_id=user_id, goal_id=goal_id, final_value=goal)
        return ManagerResult(True, "Duty has been created")

    @staticmethod
    def delete(user_id: int, goal_id: int) -> ManagerResult:
        '''
        Delete duty with given user_id, goal_id
        '''
        Duty.objects.filter(user_id=user_id, goal_id=goal_id).delete()

        return ManagerResult(True, "Duty deleted successfully!")
