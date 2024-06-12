"""
File for defining handlers for group in Django notation
"""

from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from ..models import Group
from ..serializers import GoalSerializer, GroupSerializer
from ..permissions import GroupPermission


class GroupViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for a group model
    """

    #permission_classes = [GroupPermission]
    #queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        """
        Function to get a list of all users groups
        """

        user = self.request.user
        return Group.objects.filter(Q(users__in=[user]) | Q(leader=user))

    @action(methods=["get"], detail=True)
    def goals(self, request, pk):
        goals = Group.objects.get(pk=pk).goals_group.all()
        return Response(
            GoalSerializer(goals, many=True).data,
            status=status.HTTP_200_OK
        )
