'''
Module for handling duty records in db
'''

from goald_app.managers.common import ManagerResult
from goald_app.models import Duty


class DutyManager:
    '''
    Manager for handling duties in table
    '''

    @staticmethod
    def get_all() -> list:
        '''
        Get all duties from the table
        '''
        return Duty.objects.all()

    @staticmethod
    def create(user_id: int, goal_id: int, final_value: int) -> ManagerResult:
        '''
        Create a duty with given user_id, goal_id, final_value
        '''
        if Duty.objects.filter(user_id=user_id, goal_id=goal_id).exists():
            return ManagerResult(False, "Duty already exists!")

        Duty.objects.create(user_id=user_id, goal_id=goal_id, final_value=final_value)
        return ManagerResult(True, "Duty has been created")

    @staticmethod
    def pay(user_id: int, goal_id: int, value: int) -> ManagerResult:
        '''
        Pay a some value
        '''
        try:
            Duty.objects.get(user_id=user_id, goal_id=goal_id).current_value += value
        except Duty.DoesNotExist:
            pass

        return ManagerResult(False, "No duty found!")

    @staticmethod
    def delegate(
        user_id: int, goal_id: int, delegate_id: int, value: int
    ) -> ManagerResult:
        '''
        Delegate a duty to someone
        '''
        try:
            Duty.objects.get(user_id=user_id, goal_id=goal_id)

            try:
                Duty.objects.get(
                    user_id=delegate_id, goal_id=goal_id
                ).final_value += value
            except Duty.DoesNotExist:
                Duty.objects.create(
                    user_id=delegate_id, goal_id=goal_id, final_value=value
                )

        except Duty.DoesNotExist:
            pass

        return ManagerResult(False, "No duty found!")

    @staticmethod
    def delete(user_id: int, goal_id: int) -> ManagerResult:
        '''
        Delete duty with given user_id, goal_id
        '''
        Duty.objects.filter(user_id=user_id, goal_id=goal_id).delete()

        return ManagerResult(True, "Duty deleted successfully!")
