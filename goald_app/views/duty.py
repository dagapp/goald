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
