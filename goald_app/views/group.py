"""
File for defining handlers for group in Django notation
"""

from django.db.models import Q

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..models import Group
from ..serializers import GroupSerializer
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

