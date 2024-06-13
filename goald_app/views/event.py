"""
File for defining handlers for event in Django notation
"""

from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import viewsets, serializers, status

from ..models import Group, Event
from ..serializers import EventSerializer
from ..permissions import EventPermission
from ..paginations import EventViewPagination


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ModelViewSet for an event model
    """

    serializer_class = EventSerializer
    permission_classes = [EventPermission]
    pagination_class = EventViewPagination

    def get_queryset(self):
        """
        Handler for getting events of group
        """
        user = self.request.user
        groups = user.users_groups.all() | user.led_group.all()
        return Event.objects.filter(group__in=groups)

