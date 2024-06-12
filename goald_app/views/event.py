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
        queryset = []
        user = self.request.user

        groups = Group.objects.filter(Q(users__in=[user]) | Q(leader=user))

        filter_queryset = Q()
        for group in groups:
            filter_queryset = filter_queryset | Q(group=group)

        queryset = Event.objects.filter(filter_queryset)


        return queryset
