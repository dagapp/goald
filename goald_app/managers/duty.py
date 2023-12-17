"""
Module for handling duty records in db
"""

from goald_app.managers.common import DoesNotExist, AlreadyExists
from goald_app.models import Duty


class DutyManager:
    """
    Manager for handling duties in table
    """

    @staticmethod
    def get_all() -> any:
        """
        Get all duties from the table
        """
        return Duty.objects.all()

    @staticmethod
    def create(user_id: int, goal_id: int, final_value: int) -> None:
        """
        Create a duty with given user_id, goal_id, final_value
        """
        if Duty.objects.filter(user_id=user_id, goal_id=goal_id).exists():
            raise AlreadyExists

        Duty.objects.create(user_id=user_id, goal_id=goal_id, final_value=final_value)

    @staticmethod
    def pay(user_id: int, goal_id: int, value: int) -> None:
        """
        Pay a some value
        """
        try:
            Duty.objects.get(user_id=user_id, goal_id=goal_id).current_value += value
        except Duty.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def delegate(
        user_id: int, goal_id: int, delegate_id: int, value: int
    ) -> None:
        """
        Delegate a duty to someone
        """
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

        except Duty.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def delete(user_id: int, goal_id: int) -> None:
        """
        Delete duty with given user_id, goal_id
        """
        try:
            Duty.objects.filter(user_id=user_id, goal_id=goal_id).delete()
        except Duty.DoesNotExist as e:
            raise DoesNotExist from e
