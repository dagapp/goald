"""
File for defining handlers for group in Django notation
"""

from django.urls import reverse
from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from ..models import Group
from ..serializers import UserSerializer, GoalSerializer, GroupSerializer, EventSerializer
from ..permissions import GroupPermission
from ..paginations import GroupViewSetPagination


class GroupViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for a group model
    """

    #queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [GroupPermission]
    pagination_class = GroupViewSetPagination

    def get_queryset(self):
        """
        Function to get a list of all users groups
        """

        user = self.request.user
        groups = user.users_groups.all() | user.led_group.all()
        return groups

    @action(methods=["get"], detail=True)
    def users(self, request, pk):
        group = Group.objects.get(pk=pk)
        return Response(
            {
                "leader": UserSerializer(group.leader).data,
                "participants": UserSerializer(group.users.all(), many=True).data
            },
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True)
    def invite(self, request, pk):
        group = Group.objects.get(pk=pk)
        if request.user != group.leader:
            return Response(
                {"detail": "You are not a leader"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {"detail": reverse("group-join", args=[""]) + group.token},
            status=status.HTTP_200_OK
        )

    @action(methods=["post"], detail=True)
    def join(self, request, pk):
        group = Group.objects.get(pk=pk)
        if group is None:
            return Response(
                {"detail": "Group doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not group.is_public:
            return Response(
                {"detail": "Group is not public"},
                status=status.HTTP_400_BAD_REQUEST
            )

        group.users.add(request.user)

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )

    @action(methods=["post"], detail=False, url_path=r"join/(?P<token>(\w|\-)+)", url_name="join")
    def join_token(self, request, token):
        group = Group.objects.get(token=token)
        if group is None:
            return Response(
                {"detail": "Group doesn't exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        group.users.add(request.user)

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True)
    def goals(self, request, pk):
        goals = Group.objects.get(pk=pk).goals.all()
        return Response(
            GoalSerializer(goals, many=True).data,
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True)
    def events(self, request, pk):
        events = Group.objects.get(pk=pk).events.all()
        return Response(
            EventSerializer(events, many=True).data,
            status=status.HTTP_200_OK
        )
