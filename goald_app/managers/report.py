'''
Module for handling report records in table
'''

from goald_app.managers.common import DoesNotExist
from goald_app.models import Report, Goal


class ReportManager():
    '''
    Manager to handle reports in table
    '''
    @staticmethod
    def get_all(goal_id: int) -> any:
        '''
        Get all reports for given goal_id
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            raise DoesNotExist

        return Report.objects.filter(goal_id=goal_id)

    @staticmethod
    def get(report_id: int) -> any:
        '''
        Get a report with given report_id
        '''
        try:
            return Report.objects.get(id=report_id)
        except Report.DoesNotExist as e:
            raise DoesNotExist from e

    @staticmethod
    def exists(report_id: int) -> bool:
        '''
        Check if report exists
        '''
        return Report.objects.filter(report_id=report_id).exists()

    @staticmethod
    def create(goal_id: int, text: str, proof: str) -> None:
        '''
        Create a report with given goal_id, text and proof
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            raise DoesNotExist

        Report.objects.create(goal_id=goal_id, text=text, proof=proof)

    @staticmethod
    def text(report_id: int, text: str = None) -> str:
        '''
        Set/get a text value
        '''
        if not Report.objects.filter(id=report_id).exists():
            raise DoesNotExist

        if text is not None:
            Report.objects.get(id=report_id).text = text
        
        return Report.objects.get(id=report_id).text

    @staticmethod
    def proof(report_id: int, proof: str = None) -> str:
        '''
        Set/get a proof value
        '''
        if not Report.objects.get(id=report_id).exists():
            raise DoesNotExist

        if proof is not None:
            Report.objects.get(id=report_id).proof = proof

        return Report.objects.get(id=report_id).proof

    @staticmethod
    def delete(report_id: int) -> None:
        '''
        Delete report with given report_id
        '''
        if not Report.objects.filter(id=report_id).exists():
            raise DoesNotExist

        Report.objects.get(id=report_id).delete()
