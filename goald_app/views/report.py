"""
File for defining handlers for group in Django notation
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from ..models import User, Report
from ..serializers import ReportSerializer

class ReportView(APIView):
    def get(self, request):
        """
        Handler for reading the report info
        """

        if not User.objects.get(id=request.session["id"]).groups.goals.reports.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "You have no permission to have this info"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        report = Report.objects.get(id=request.GET["id"])
        return Response(
            data=ReportSerializer(instance=report).data,
            status=status.HTTP_200_OK
        )


    def post(self, request):
        """
        Handler for creating a report
        """

        report = ReportSerializer(data=request.data)

        if Report.objects.filter(**request.data).exists():
            #TODO: check out how it works and maybe switch "return Response" with it
            raise serializers.ValidationError("This report already exists")

        if not report.is_valid():
            return Response(
                data={"detail": "Report data is not valid"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        report.save()
        return Response(
            data={"detail", f"Report id: {report.data['id']}"},
            status=status.HTTP_201_CREATED
        )
        

    def patch(self, request):
        """
        Handler for updating the report info
        """

        report = ReportSerializer(data=request.data)

        if not Report.objects.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "Report with given id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if not User.obejcts.filter(id=request.session["id"]).groups.goals.reports.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "You have no permission to change report info"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        Report.objects.get(id=request.GET["id"]).update(report)

        return Response(
            data={"detail": "Report info updated"},
            status=status.HTTP_200_OK
        )


    def delete(self, request):
        """
        Handler for deleting the report
        """

        if not Report.objects.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "Report with given id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if not User.obejcts.filter(id=request.session["id"]).groups.goals.reports.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "You have no permission to delete this report"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        Report.objects.get(id=request.GET["id"]).delete()

        return Response(
            data={"detail": "Report deleted"},
            status=status.HTTP_200_OK
        )
