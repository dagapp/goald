"""
File for defining handlers for goal in Django notation
"""

from django.db.models import Q

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from ..models import Group, Goal, Duty, Report
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

    @action(methods=["post"], detail=True)
    def distribute(self, request, pk):
        goal = Goal.objects.get(pk=pk)

        group = goal.group
        if request.user != group.leader:
            return Response(
                {"detail": "You are not a leader"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        leader = group.leader
        users = group.users

        final_value = goal.final_value

        users_count = users.count() + 1 #for leader

        participant_final_value = final_value // users_count
        leader_final_value = final_value - participant_final_value * (users_count - 1)

        leader_duty = Duty.objects.filter(goal=goal, user=leader)
        leader_duty.update(final_value=leader_final_value)
        leader_duty = leader_duty.first()

        for user in users.all():
            duty = Duty.objects.filter(goal=goal, user=user)
            if not duty.exists():
                Duty.objects.create(
                    final_value=participant_final_value,
                    current_value=0,
                    deadline=getattr(leader_duty, "deadline"),
                    alert_period=getattr(leader_duty, "alert_period"),
                    user=user,
                    goal=goal
                )
            else:
                duty.update(final_value=participant_final_value)

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )

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

