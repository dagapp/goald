"""
File for defining permission classes
"""

from django.db.models import Q

from rest_framework import permissions

from .models import Group


class NotAuthenticated(permissions.BasePermission):
    """
    Permission class for checking not authenticated users
    """

    def has_permission(self, request, view):
        return not request.user.is_authenticated


class GroupLeaderPermission(permissions.IsAuthenticated):
    """
    Permission class for group leaders
    """
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.leader
    

class GoalGroupLeaderPermission(permissions.IsAuthenticated):
    """
    Permission class for group leaders
    """
    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.group.leader
    

class GroupPermission(permissions.IsAuthenticated):
    """
    Permission class for group
    """

    def has_object_permission(self, request, view, obj):
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


class ImagePermission(permissions.IsAuthenticated):
    """
    Permission class for image
    """
    
    def has_object_permission(self, request, view, obj):
        """
        Function for checking image object permissions
        """

        user = request.user

        group = obj.group
        if obj.report is not None:
            group = obj.report.goal.group

        if group is None:
            return False

        return user == group.leader or user in group.users.all()
