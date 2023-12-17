"""
Module for handling goal records in db
"""

import datetime

from goald_app.managers.common import DoesNotExist, AlreadyExists
from goald_app.models import Group, Goal, Duty


class GoalManager:
    """
    Manager for handling goals in table
    """

    @staticmethod
    def get_all(user_id: int) -> any:
        """
        Get all goals for given user_id
        """
        try:
            result = []
            groups = Group.objects.filter(users__id=user_id)
            for group in groups:
                result += Goal.objects.filter(group_id=group)

            return result

        except Goal.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def get(user_id: int, goal_id: int) -> any:
        """
        Get a goal with given id from the table
        """
        try:
            return Group.objects.filter(users__id=user_id).goals.get(goal_id=goal_id)

        except Goal.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def exists(goal_id: int) -> bool:
        """
        Check if goal exists
        """
        return Goal.objects.filter(goal_id=goal_id).exists()

    @staticmethod
    def create(
        name: str,
        group_id: int,
        final_value: int = 0,
        deadline: datetime.datetime = None,
        alert_period: datetime.time = None,
        # supergoal_id: int,
    ) -> None:
        """
        Create a goal and start it
        """
        if not Group.objects.filter(id=group_id).exists():
            raise DoesNotExist

        group = Group.objects.get(id=group_id)

        if Goal.objects.filter(name=name, group=group).exists():
            raise AlreadyExists

        goal = Goal.objects.create(
            name=name,
            deadline=deadline,
            alert_period=alert_period,
            group=group,
            # supergoal_id=supergoal_id,
        )

        Duty.objects.create(
            final_value=final_value,
            current_value=final_value,
            deadline=deadline,
            alert_period=alert_period,
            user=group.leader,
            goal=goal,
        )

    @staticmethod
    def start(goal_id: int) -> None:
        """
        Start a goal
        """
        if not Goal.objects.filter(id=goal_id).exists():
            raise DoesNotExist

        Goal.objects.get(id=goal_id).is_active = True

    @staticmethod
    def finish(goal_id: int) -> None:
        """
        Finish a goal
        """
        if not Goal.objects.filter(id=goal_id).exists():
            raise DoesNotExist

        Goal.objects.get(id=goal_id).is_active = False

    @staticmethod
    def deadline(goal_id: int, deadline: datetime.datetime = None) -> datetime.datetime:
        """
        Set/get a deadline value
        """
        if not Goal.objects.filter(id=goal_id).exists():
            raise DoesNotExist

        if deadline is not None:
            Goal.objects.get(id=goal_id).deadline = deadline

        return Goal.objects.get(id=goal_id).deadline

    @staticmethod
    def alert_period(
        goal_id: int, alert_perion: datetime.timedelta = None
    ) -> datetime.datetime:
        """
        Set/get an alert_perion value
        """
        try:
            goal = Goal.objects.get(id=goal_id)

            if alert_perion is not None:
                goal.alert_period = alert_perion

            return goal.alert_period
        except Goal.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def delete(goal_id: int) -> None:
        """
        Delete the goal
        """
        try:
            goal = Goal.objects.get(id=goal_id)
            Duty.objects.filter(goal_id=goal_id).delete()
            goal.delete()
        except Goal.DoesNotExist as e:
            raise DoesNotExist from e
