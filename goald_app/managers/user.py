"""
Module for handling user records in db
"""

from bcrypt import gensalt, hashpw

from goald_app.managers.common import DoesNotExist, AlreadyExists, IncorrectData

from goald_app.models import User

LENGTH_SALT = 29
LENGTH_HASH = 60


class UserManager:
    """
    Manager for handling users in table
    """

    @staticmethod
    def get_all() -> any:
        """
        Get all users from the table
        """
        return User.objects.all()

    @staticmethod
    def get(login: str) -> any:
        """
        Get a users with given login from the table
        """
        try:
            return User.objects.get(login=login)
        except User.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def exists(*args, **kwds) -> bool:
        """
        Check wheteher a user with given id exists
        """
        if "user_id" in kwds:
            if "login" in kwds:
                return User.objects.filter(id=kwds["user_id"], login=kwds["login"]).exists()
            else:
                return User.objects.filter(id=kwds["user_id"]).exists()
        else:
            if "login" in kwds:
                return User.objects.filter(login=kwds["login"]).exists()
            else:
                raise IncorrectData

    @staticmethod
    def auth(login: str, password: str) -> None:
        """
        Auth a user with given login and password
        """
        try:
            user = User.objects.get(login=login)

            salt = user.password[:LENGTH_SALT]
            salted_hash = hashpw(bytes(password, "utf-8"), salt)

            if salted_hash != user.password:
                raise IncorrectData
        except User.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def create(login: str, password: str) -> None:
        """
        Create a user with given login and password
        """
        if User.objects.filter(login=login).exists():
            raise AlreadyExists

        salt = gensalt()
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        User.objects.create(login=login, password=salted_hash)

    @staticmethod
    def change_password(user_id: int, password: str) -> None:
        """
        Change a user's password with given login and new password
        """
        try:
            user = User.objects.get(id=user_id)
            user.password = hashpw(bytes(password, "utf-8"), user.password[:LENGTH_SALT])
            user.save()
        except User.DoesNotExist:
            raise DoesNotExist

    @staticmethod
    def delete(user_id: int) -> None:
        """
        Delete the user with given id
        """
        try:
            User.objects.filter(id=user_id).delete()
        except User.DoesNotExist:
            raise DoesNotExist
