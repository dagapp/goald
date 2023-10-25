'''
Module for handling report records in table
'''

from goald_app.managers.manager import ManagerResult
from goald_app.models import Report


class ReportManager():
    '''
    Manager to handle reports in table
    '''
    @staticmethod
    def objects_all() -> list:
        '''
        Get all reports from the table
        '''
        return Report.objects.all()

    @staticmethod
    def create(goal_id: int, text: str, proof: bytes) -> ManagerResult:
        '''
        Create a report with given goal_id, text and proof
        '''
        if Report.objects.filter(goal_id=goal_id).exists():
            return ManagerResult(False, "Report already exists!")

        Report.objects.create(goal_id=goal_id, text=text, proof=proof)
        return ManagerResult(True, "Report has been created")

    @staticmethod
    def delete(goal_id: int) -> ManagerResult:
        '''
        Delete report with given goal_id
        '''
        Report.objects.filter(goal_id=goal_id).delete()

        return ManagerResult(True, "Report deleted successfully!")
