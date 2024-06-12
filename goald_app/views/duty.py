"""
File for defining handlers for group in Django notation
"""

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from ..models import Duty
from ..serializers import DutySerializer
from ..paginations import DutyViewSetPagination


class DutyViewSet(viewsets.ModelViewSet):
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
