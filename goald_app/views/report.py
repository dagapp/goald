"""
File for defining handlers for report in Django notation
"""
from django.db.models import Q

from rest_framework import viewsets

from ..models import Report, Goal, Group
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
        group = Group.objects.filter(Q(users__in=[user]) | Q(leader=user))

        return Report.objects.filter(
            goal__in=Goal.objects.filter(group__in=group)
        )
    