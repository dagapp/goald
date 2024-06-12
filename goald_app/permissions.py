"""
File for defining permission classes
"""

from django.db.models import Q

from rest_framework import permissions

from .models import Group


class GroupPermission(permissions.BasePermission):
    """
    Permission class for group
    """

    def has_objects_permission(self, request, view, obj):
        """
        Function for defining group object permissions
        """

        user = request.user
        return (user in obj.users) or (user == obj.leader)
