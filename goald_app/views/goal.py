"""
File for defining handlers for goal in Django notation
"""

from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..models import Group, Goal
from ..serializers import GoalSerializer


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