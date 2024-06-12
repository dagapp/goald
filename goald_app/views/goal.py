"""
File for defining handlers for goal in Django notation
"""

from django.db.models import Q

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from ..models import Group, Goal, Report
from ..serializers import GoalSerializer, ReportSerializer


class GoalViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for a goal model
    """

    serializer_class = GoalSerializer

    def get_queryset(self):
        """
        Function to get a list of all users goals
        """

        user = self.request.user
        return Goal.objects.filter(
            group__in=Group.objects.filter(Q(users__in=[user]) | Q(leader=user))
        )

    @action(methods=["get"], detail=True)
    def reports(self, request, pk):
        reports = Report.objects.filter(Q(goal=pk))
        return Response(
            ReportSerializer(reports, many=True).data,
            status=status.HTTP_200_OK
        )
    