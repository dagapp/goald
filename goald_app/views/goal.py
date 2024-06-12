"""
File for defining handlers for goal in Django notation
"""

from django.db.models import Q

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from ..models import Group, Goal, Report
from ..serializers import GoalSerializer, ReportSerializer, EventSerializer
from ..paginations import GoalViewSetPagination

class GoalViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for a goal model
    """

    serializer_class = GoalSerializer
    pagination_class = GoalViewSetPagination

    def get_queryset(self):
        """
        Function to get a list of all users goals
        """

        user = self.request.user
        groups = user.users_groups.all() | user.led_group.all()
        return Goal.objects.filter(group__in=groups)

    @action(methods=["get"], detail=True)
    def reports(self, request, pk):
        reports = Report.objects.filter(goal=pk)
        return Response(
            ReportSerializer(reports, many=True).data,
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True)
    def events(self, request, pk):
        events = Goal.objects.get(pk=pk).events.all()
        return Response(
            EventSerializer(events, many=True).data,
            status=status.HTTP_200_OK
        )

