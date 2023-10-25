from .manager import ManagerResult
from ..models import Duty


class DutyManager():
    @staticmethod
    def objects_all() -> list:
        return Duty.objects.all()

    @staticmethod
    def create(user_id: int, goal_id: int, goal: int) -> ManagerResult:
        if Duty.objects.filter(user_id=user_id, goal_id=goal_id).exists():
            return ManagerResult(False, "Duty already exists!")

        Duty.objects.create(user_id=user_id, goal_id=goal_id, final_value=goal)
        return ManagerResult(True, "Duty has been created")

    @staticmethod
    def delete(user_id: int, goal_id: int) -> ManagerResult:
        Duty.objects.filter(user_id=user_id, goal_id=goal_id).delete()

        return ManagerResult(True, "User deleted successfully!")
