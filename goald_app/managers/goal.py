'''
Module for handling goal records in db
'''

import datetime

from goald_app.managers.common import ManagerResult
from goald_app.models import User, Group, Goal, Duty


class GoalManager:
    '''
    Manager for handling goals in table
    '''

    @staticmethod
    def get_all(user_id: int) -> ManagerResult:
        '''
        Get all goals for given user_id
        '''
        try:
            result = []
            groups = Group.objects.filter(users__id=user_id)
            for group in groups:
                result += Goal.objects.filter(group_id=group)

            if result:
                return ManagerResult(True, "", result)

        except Goal.DoesNotExist:
            pass

        return ManagerResult(False, "No goals found!")

    @staticmethod
    def get(user_id: int, goal_id: int) -> ManagerResult:
        '''
        Get a goal with given id from the table
        '''
        try:
            users = User.objects.filter(
                id=user_id, groups__id=Group.objects.filter(goal__id=goal_id)[0].id
            )
            if users:
                result = Goal.objects.filter(id=goal_id)
                return ManagerResult(True, "", result)

        except Goal.DoesNotExist:
            pass

        return ManagerResult(False, "No goal found!")

    @staticmethod
    def exists(goal_id: int) -> ManagerResult:
        '''
        Check if goal exists
        '''
        if Goal.objects.filter(goal_id=goal_id).exists():
            return ManagerResult(True, "Goal exists")

        return ManagerResult(False, "Goal doesnt exist!")

    @staticmethod
    def create(
        name: str,
        group_id: int,
        final_value: int = 0,
        deadline: datetime.datetime = None,
        alert_period: datetime.time = None,
        # supergoal_id: int,
    ) -> ManagerResult:
        '''
        Create a goal and start it
        '''
        if not Group.objects.filter(id=group_id).exists():
            return ManagerResult(False, "Group with id={group_id} doesnt exist!")

        if Goal.objects.filter(name=name, group_id=group_id).exists():
            return ManagerResult(False, "Goal already exists!")

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
            user_id=Group.objects.get(id=group_id).leader_id,
            goal_id=goal,
        )

        return ManagerResult(True, "Goal created successfully!")

    @staticmethod
    def start(goal_id: int) -> ManagerResult:
        '''
        Start a goal
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            return ManagerResult(False, "Goal doesn't exist!")

        Goal.objects.get(id=goal_id).is_active = True

        return ManagerResult(True, "Goal finished successfully")

    @staticmethod
    def finish(goal_id: int) -> ManagerResult:
        '''
        Finish a goal
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            return ManagerResult(False, "Goal doesn't exist!")

        Goal.objects.get(id=goal_id).is_active = False

        return ManagerResult(True, "Goal finished successfully")

    @staticmethod
    def deadline(goal_id: int, deadline: datetime.datetime = None) -> ManagerResult:
        '''
        Set/get a deadline value
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            return ManagerResult(False, "Goal doesn't exist!")

        if deadline is None:
            return ManagerResult(
                True,
                "Goal's deadline get successfully",
                Goal.objects.get(id=goal_id).deadline,
            )

        Goal.objects.get(id=goal_id).deadline = deadline
        return ManagerResult(True, "Goal's deadline set successfully")

    @staticmethod
    def alert_period(
        goal_id: int, alert_perion: datetime.timedelta = None
    ) -> ManagerResult:
        '''
        Set/get an alert_perion value
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            return ManagerResult(False, "Goal doesn't exist!")

        if alert_perion is None:
            return ManagerResult(
                True,
                "Goal's alert period get successfully",
                Goal.objects.get(id=goal_id).alert_period,
            )

        Goal.objects.get(id=goal_id).alert_period = alert_perion
        return ManagerResult(True, "Goal's alert period set successfully")

    @staticmethod
    def delete(goal_id: int) -> ManagerResult:
        '''
        Delete the goal
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            return ManagerResult(False, "Goal doesn't exist!")

        Duty.objects.filter(goal_id=goal_id).delete()

        Goal.objects.get(id=goal_id).delete()

        return ManagerResult(True, "Goal has been successfully deleted")
