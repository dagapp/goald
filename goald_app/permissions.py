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


class ImagePermission(permissions.BasePermission):
    """
    Permission class for image
    """
    def has_permission(self, request, view):
        """
        Function for checking image general permission
        """

        print(f"has_permission: {view.action}")
        return True
    
    def has_object_permission(self, request, view, obj):
        """
        Function for checking image object permissions
        """

        print(f"has_objects_permission: {view.action}")
        user = request.user

        if obj.group is not None:
            print("Group is not NULL")
            group = obj.group
            return user == group.leader or group.users.filter(id=user.id).exists()
        elif obj.report is not None:
            print("Report is not NULL")
            group = obj.report.goal.group
            return user == group.leader or group.users.filter(id=user.id).exists()
        else:
            return False
