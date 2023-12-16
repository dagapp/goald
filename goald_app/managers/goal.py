'''
Module for handling goal records in table
'''

from goald_app.managers.manager import ManagerResult, AuthManager
from goald_app.models import User, Group, Goal


class GoalManager():
    '''
    Manager to handle goals in table
    '''
    @staticmethod
    def objects_all() -> ManagerResult:
        '''
        Get all goals from the table
        '''
        try:
            result = []
            groups = Group.objects.filter(users__id=AuthManager.user_id)
            for group in groups:
                result += Goal.objects.filter(group_id=group)

            if result:
                return ManagerResult(True, "", result)

        except Goal.DoesNotExist:
            pass

        return ManagerResult(False, "No goals found!")

    @staticmethod
    def objects_get(goal_id: int) -> ManagerResult:
        '''
        Get a goal with given id from the table
        '''
        try:
            users = User.objects.filter(id=AuthManager.user_id,
                                        groups__id=Group.objects.filter(goal__id=goal_id)[0].id)
            if users:
                result = Goal.objects.filter(id=goal_id)
                return ManagerResult(True, "", result)

        except Goal.DoesNotExist:
            pass

        return ManagerResult(False, "No goal found!")
    
    @staticmethod
    def exists(id: int) -> ManagerResult:
        if Goal.objects.filter(id=id).exists():
            return ManagerResult(True, "Goal exists")

        return ManagerResult(False, "Goal doesnt exist!")

    @staticmethod
    def create(name: str, group_id: int) -> ManagerResult:        
        if not Group.objects.filter(id=group_id).exists():
            return ManagerResult(False, "Group with id={group_id} doesnt exist!")
        
        if Goal.objects.filter(name=name, group_id=group_id).exists():
            return ManagerResult(False, "Goal already exists!")
        
        Goal.objects.create(name=name, is_active=True, group_id=group_id)
        return ManagerResult(True, "Goal created successfully!")
