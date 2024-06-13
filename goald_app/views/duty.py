"""
File for defining handlers for group in Django notation
"""

import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from ..models import Duty, Goal, Event, EventType, EVENT_MESSAGES
from ..serializers import DutySerializer
from ..paginations import DutyViewSetPagination


class DutyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ModelViewSet for a Duty model
    """

    serializer_class = DutySerializer
    pagination_class = DutyViewSetPagination

    def get_queryset(self):
        """
        Function to get a list of all users duties
        """

        user = self.request.user
        return Duty.objects.filter(user=user)

    #TODO: implement group leader check with permission_classes
    @action(methods=["post"], detail=True) #permission_classes=[AllowAny]
    def confirm(self, request, pk):
        goal = Duty.objects.get(pk=pk).goal
        group = goal.group

        if not request.user == group.leader:
            return Response(
                {"detail": "You are not a leader for a corresponding group"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        duty = Duty.object.get(pk=pk)
        current_value = getattr(duty, "current_value")
        duty.update(current_value=current_value + request.data["value"])

        if getattr(duty, "final_value") <= getattr(duty, "current_value"):
            Event.objects.create(
                type=int(EventType.UserPaid),
                text=EVENT_MESSAGES[EventType.UserPaid],
                timestamp=datetime.datetime.now(),
                group=group,
                goal=goal
            )

        if getattr(goal, "final_value") <= getattr(goal, "current_value"):
            Event.objects.create(
                type=int(EventType.GoalReached),
                text=EVENT_MESSAGES[EventType.GoalReached],
                timestamp=datetime.datetime.now(),
                group=group,
                goal=goal
            )

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )

    #TODO: implement group leader check with permission_classes
    @action(methods=["post"], detail=True) #permission_classes=[AllowAny]
    def delegate(self, request, pk):
        duty_from = Duty.objects.get(pk=pk)
        if duty_from is None:
            return Response(
                {"detail": "Incorrect duty id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        goal = duty_from.goal

        duty_to = goal.duties.get(id=request.data["duty_to"])
        if duty_to is None:
            return Response(
                {"detail": "Incorrect duty_to id"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not request.user == goal.group.leader:
            return Response(
                {"detail": "You are not a leader for a corresponding group"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        final_value_from = getattr(duty_from, "final_value")
        final_value_to   = getattr(duty_to,   "final_value")

        duty_from.update(final_value=final_value_from - request.data["value"])
        duty_to.update(final_value=final_value_to + request.data["value"])

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )
