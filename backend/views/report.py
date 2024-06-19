"""
File for defining handlers for report in Django notation
"""

from rest_framework import viewsets

from ..models import Report, Goal
from ..serializers import ReportSerializer
from ..permissions import ReportPermission
from ..paginations import ReportViewSetPagination

class ReportViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for a report model
    """

    serializer_class = ReportSerializer
    permission_classes = [ReportPermission]
    pagination_class = ReportViewSetPagination

    def get_queryset(self):
        """
        Function to get a list of all goals reports
        """

        user = self.request.user
        groups = user.users_groups.all() | user.led_group.all()

        return Report.objects.filter(
            goal__in=Goal.objects.filter(group__in=groups)
        )
