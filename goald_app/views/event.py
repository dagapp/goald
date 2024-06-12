"""
File for defining handlers for event in Django notation
"""

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
        queryset = []
        user_id = self.request.session["id"]
        group_id = self.kwargs.get("id", None)

        if not group_id:
            return queryset

        if not User.objects.get(id=user_id).groups.filter(id=group_id).exists() \
            and not Group.objects.filter(leader_id=user_id, id=group_id).exists():
            return queryset

        queryset = Event.objects.filter(group=group_id)

        return queryset
