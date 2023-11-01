'''
Module for handling user records in table
'''

from bcrypt import gensalt, hashpw

from goald_app.managers.manager import ManagerResult
from goald_app.models import User

LENGTH_SALT = 29
LENGTH_HASH = 60


class UserManager():
    '''
    Manager to handle users in table
    '''
    @staticmethod
    def objects_all() -> ManagerResult:
        '''
        Get all users from the table
        '''
        return ManagerResult(True, "", User.objects.all())

    @staticmethod
    def objects_get(login: str) -> ManagerResult:
        '''
        Get a users with given login from the table
        '''
        try:
            return ManagerResult(True, "User found", User.objects.get(login=login))
        except User.DoesNotExist:
            return ManagerResult(False, "User doesnt exist!")

    @staticmethod
    def exists(user_id: int) -> ManagerResult:
        '''
        Check wheteher a user with given id exists
        '''
        if User.objects.filter(id=user_id).exists():
            return ManagerResult(True, "User exists")

        return ManagerResult(False, "User doesnt exist!")

    @staticmethod
    def auth(login: str, password: str) -> ManagerResult:
        '''
        Auth a user with given login and password
        '''
        user = None
        try:
            user = User.objects.get(login=login)
        except User.DoesNotExist:
            return ManagerResult(False, "Incorrect login or password!")

        salt = user.password[:LENGTH_SALT]
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        if salted_hash != user.password:
            return ManagerResult(False, "Incorrect login or password!")

        return ManagerResult(True, "User authenticated successfully!")

    @staticmethod
    def deauth(_id: int) -> ManagerResult:
        '''
        Deauth the user with given id
        '''
        return ManagerResult(True, "User successfully deauthenticated!")

    @staticmethod
    def create(login: str, password: str) -> ManagerResult:
        '''
        Create a user with given login and password
        '''
        if User.objects.filter(login=login).exists():
            return ManagerResult(False, "User already exists!")

        salt = gensalt()
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        User.objects.create(login=login, password=salted_hash)

        return ManagerResult(True, "User created successfully!")

    @staticmethod
    def change(_id: int, password: str) -> ManagerResult:
        '''
        Change a user's password with given login and new password
        '''
        user = User.objects.get(id=_id)
        user.password = hashpw(bytes(password, "utf-8"), user.password[:LENGTH_SALT])
        user.save()

        return ManagerResult(True, "Users password changed successfully!")

    @staticmethod
    def delete(_id: int) -> ManagerResult:
        '''
        Delete the user with given id
        '''
        User.objects.filter(id=_id).delete()

        return ManagerResult(True, "User deleted successfully!")
