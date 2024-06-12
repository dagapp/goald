"""
File for defining handlers for event in Django notation
"""

from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import serializers, status

from ..models import Group, Event
from ..serializers import EventSerializer
from ..paginations import EventViewPagination


class EventView(ListAPIView):
    """
       A view for handling events
    """
    serializer_class = EventSerializer
    pagination_class = EventViewPagination

    def get_queryset(self):
        """
        Handler for getting events of group
        """
        user = self.request.user
        groups = Group.objects.filter(Q(users__in=[user]) | Q(leader=user))
        return Event.objects.filter(Q(group__in=groups))

