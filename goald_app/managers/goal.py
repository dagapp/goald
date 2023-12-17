"""
Module for handling goal records in db
"""

import datetime


from goald_app.managers.common import DoesNotExist, AlreadyExists
from goald_app.models import User, Group, Goal, Duty


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

            if result:
                return result

        except Goal.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def get(user_id: int, goal_id: int) -> any:
        """
        Get a goal with given id from the table
        """
        try:
            users = User.objects.filter(
                id=user_id, groups__id=Group.objects.filter(goal__id=goal_id)[0].id
            )
            if users:
                result = Goal.objects.filter(id=goal_id)
                return result

        except Goal.DoesNotExist:
            DoesNotExist

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

        if Goal.objects.filter(name=name, group_id=group_id).exists():
            raise AlreadyExists

        goal = Goal.objects.create(
            name=name,
            deadline=deadline,
            alert_period=alert_period,
            group_id=Group.objects.get(id=group_id),
            # supergoal_id=supergoal_id,
        )

        Duty.objects.create(
            final_value=final_value,
            current_value=final_value,
            deadline=deadline,
            alert_period=alert_period,
            user_id=Group.objects.get(id=group_id).leader,
            goal_id=goal,
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
    def deadline(
        goal_id: int, deadline: datetime.datetime = None
    ) -> datetime.datetime | None:
        """
        Set/get a deadline value
        """
        if not Goal.objects.filter(id=goal_id).exists():
            raise DoesNotExist

        if deadline is None:
            return Goal.objects.get(id=goal_id).deadline

        Goal.objects.get(id=goal_id).deadline = deadline

    @staticmethod
    def alert_period(
        goal_id: int, alert_perion: datetime.timedelta = None
    ) -> datetime.datetime | None:
        """
        Set/get an alert_perion value
        """
        try:
            goal = Goal.objects.get(id=goal_id)

            if alert_perion is None:
                return goal.alert_period

            goal.alert_period = alert_perion
        except Goal.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def delete(goal_id: int) -> None:
        """
        Delete the goal
        """
        try:
            goal = Goal.objects.get(id=goal_id)
            Duty.objects.filter(goal_id=goal_id).delete()
            goal.delete()
        except Goal.DoesNotExist:
            raise DoesNotExist

