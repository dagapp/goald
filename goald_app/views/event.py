"""
File for defining handlers for event in Django notation
"""

from rest_framework import viewsets

from ..models import  Event
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
