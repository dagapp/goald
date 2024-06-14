"""
File for defining handlers for goal in Django notation
"""

import datetime

from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from ..models import  Goal, Duty, Report, Event, EventType, EVENT_MESSAGES
from ..serializers import GoalSerializer, ReportSerializer, EventSerializer
from ..permissions import GoalGroupLeaderPermission, GoalPermission
from ..paginations import GoalViewSetPagination

class GoalViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for a goal model
    """

    serializer_class = GoalSerializer
    permission_classes = [GoalPermission]
    pagination_class = GoalViewSetPagination

    def get_queryset(self):
        """
        Function to get a list of all users goals
        """

        user = self.request.user
        groups = user.users_groups.all() | user.led_group.all()
        return Goal.objects.filter(group__in=groups)

    @action(methods=["post"], detail=True, permission_classes=[GoalGroupLeaderPermission])
    def confirm(self, request, pk):
        """
        Сonfirm proc
        """

        goal = Goal.objects.get(pk=pk)
        group = goal.group

        user = User.objects.get(id=request.data["user"])
        duty = Duty.objects.get(goal=goal, user=user)

        duty.current_value += request.data["value"]
        duty.save()

        if duty.final_value <= duty.current_value:
            Event.objects.create(
                type=int(EventType.USER_PAID),
                text=EVENT_MESSAGES[EventType.USER_PAID],
                timestamp=datetime.datetime.now(),
                group=group,
                goal=goal
            )

        if goal.final_value <= goal.current_value:
            Event.objects.create(
                type=int(EventType.GOAL_REACHED),
                text=EVENT_MESSAGES[EventType.GOAL_REACHED],
                timestamp=datetime.datetime.now(),
                group=group,
                goal=goal
            )

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )

    @action(methods=["post"], detail=True, permission_classes=[GoalGroupLeaderPermission])
    def delegate(self, request, pk):
        """
        Delegate proc
        """

        goal = Goal.objects.get(pk=pk)

        user_from = User.objects.get(id=request.data["user_from"])
        if user_from is None:
            return Response(
                {"detail": "Incorrect user_from id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        duty_from = Duty.objects.get(goal=goal, user=user_from)
        if duty_from is None:
            return Response(
                {"detail": "Incorrect user_from id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_to = User.objects.get(id=request.data["user_to"])
        if user_to is None:
            return Response(
                {"detail": "Incorrect user_to id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        duty_to = Duty.objects.get(goal=goal, user=user_to)
        if duty_to is None:
            return Response(
                {"detail": "Incorrect user_to id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        value = request.data["value"]

        duty_from.final_value -= value
        duty_to.final_value   += value

        duty_from.save()
        duty_to.save()

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )

    @action(methods=["post"], detail=True, permission_classes=[GoalGroupLeaderPermission])
    def distribute(self, request, pk):
        """
        Distribute proc
        """

        goal = Goal.objects.get(pk=pk)

        group = goal.group

        leader = group.leader
        users = group.users

        final_value = goal.final_value

        users_count = users.count() + 1 #for leader

        participant_final_value = final_value // users_count
        leader_final_value = final_value - participant_final_value * (users_count - 1)

        leader_duty = Duty.objects.get(goal=goal, user=leader)
        leader_duty.final_value = leader_final_value
        leader_duty.save()

        for user in users.all():
            duty = Duty.objects.filter(goal=goal, user=user)
            if not duty.exists():
                Duty.objects.create(
                    final_value=participant_final_value,
                    current_value=0,
                    deadline=leader_duty.deadline,
                    alert_period=leader_duty.alert_period,
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
        """
        Reports proc
        """

        reports = Report.objects.filter(goal=pk)
        return Response(
            ReportSerializer(reports, many=True).data,
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True)
    def events(self, request, pk):
        """
        Events proc
        """

        events = Goal.objects.get(pk=pk).events.all()
        return Response(
            EventSerializer(events, many=True).data,
            status=status.HTTP_200_OK
        )
