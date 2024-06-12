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

    def has_permission(self, request, view):
        """
        Function for checking group general permission
        """

        print(f"has_permission: {view.action}")
        return True

    def has_objects_permission(self, request, view, obj):
        """
        Function for checking group object permissions
        """

        print(f"has_objects_permission: {view.action}")
        user = request.user

        if view.action == "retrieve":
            return user == obj.leader or user in obj.users
        elif view.action in ["update", "partial_update", "destroy"]:
            return user == obj.leader
        else:
            return False
