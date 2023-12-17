'''
Module for handling report records in table
'''

from goald_app.managers.common import ManagerResult
from goald_app.models import Report, Goal


class ReportManager():
    '''
    Manager to handle reports in table
    '''
    @staticmethod
    def get_all(goal_id: int) -> ManagerResult:
        '''
        Get all reports for given goal_id
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            return ManagerResult(False, "Goal with id={goal_id} doesnt exist!")
        
        result = Report.objects.filter(goal_id=goal_id) 
        return ManagerResult(True, "", result)
    
    @staticmethod
    def get(report_id: int) -> ManagerResult:
        '''
        Get a report with given report_id
        '''
        try:
            return ManagerResult(True, "Report found", Report.objects.get(id=report_id))
        except Report.DoesNotExist:
            pass

        return ManagerResult(False, "Report doesnt exist!")
        
    @staticmethod
    def create(goal_id: int, text: str, proof: str) -> ManagerResult:
        '''
        Create a report with given goal_id, text and proof
        '''
        if not Goal.objects.filter(id=goal_id).exists():
            return ManagerResult(False, "Goal with id={goal_id} doesnt exist!")

        Report.objects.create(goal_id=goal_id, text=text, proof=proof)
        return ManagerResult(True, "Report has been created")
    
    @staticmethod
    def text(report_id: int, text: str = None) -> ManagerResult:
        '''
        Set/get a text value
        '''
        if not Report.objects.filter(id=report_id).exists():
            return ManagerResult(False, "Report doesn't exist!")

        if text is None:
            return ManagerResult(
                True,
                "Record's text get successfully",
                Report.objects.get(id=report_id).text,
            )

        Report.objects.get(id=report_id).text = text
        return ManagerResult(True, "Record's text set successfully")
    
    @staticmethod
    def proof(report_id: int, proof: str = None) -> ManagerResult:
        '''
        Set/get a text value
        '''
        if not Report.objects.filter(id=report_id).exists():
            return ManagerResult(False, "Report doesn't exist!")

        if proof is None:
            return ManagerResult(
                True,
                "Record's proof get successfully",
                Report.objects.get(id=report_id).proof,
            )

        Report.objects.get(id=report_id).proof = proof
        return ManagerResult(True, "Record's proof set successfully")
    
    @staticmethod
    def delete(report_id: int) -> ManagerResult:
        '''
        Delete report with given report_id
        '''
        if not Report.objects.filter(id=report_id).exists():
            return ManagerResult(False, "Goal doesn't exist!")
        
        Report.objects.filter(id=report_id).delete()

        return ManagerResult(True, "Report deleted successfully!")
