from bcrypt import gensalt, hashpw

from .manager import ManagerResult
from ..models import User

LENGTH_SALT = 29
LENGTH_HASH = 60


class UserManager():
    @staticmethod
    def objects_all() -> ManagerResult:
        return ManagerResult(True, "", User.objects.all())
    
    @staticmethod
    def objects_get(login: str) -> ManagerResult:
        try:
            return ManagerResult(True, "User found", User.objects.get(login=login))
        except User.DoesNotExist:
             return ManagerResult(False, "User doesnt exist!")

    @staticmethod
    def exists(id: int) -> ManagerResult:
        if User.objects.filter(id=id).exists():
                return ManagerResult(True, "User exists")

        return ManagerResult(False, "User doesnt exist!")

    @staticmethod
    def auth(login: str, password: str) -> ManagerResult:
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
    def create(login: str, password: str) -> ManagerResult:
        if User.objects.filter(login=login).exists():
            return ManagerResult(False, "User already exists!")

        salt = gensalt()
        salted_hash = hashpw(bytes(password, "utf-8"), salt)

        User.objects.create(login=login, password=salted_hash)
        User.objects.create(login=login, password=salted_hash)

        return ManagerResult(True, "User created successfully!")

    @staticmethod
    def change(id: int, password: str) -> ManagerResult:
        user = User.objects.get(id=id)
        user.password = hashpw(bytes(password, "utf-8"), user.password[:LENGTH_SALT])
        user.save()

        return ManagerResult(True, "Users password changed successfully!")

    @staticmethod
    def delete(id: int) -> ManagerResult:
        User.objects.filter(id=id).delete()

        return ManagerResult(True, "User deleted successfully!")
