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


class GroupPermission(permissions.IsAuthenticated):
    """
    Permission class for group
    """

    def has_object_permission(self, request, view, obj):
        """
        Function for checking group object permissions
        """

        user = request.user

        if view.action == "retrieve":
            return user == obj.leader or user in obj.users.all()
        elif view.action in ["update", "partial_update", "destroy"]:
            return user == obj.leader

        return False


class GoalGroupLeaderPermission(permissions.IsAuthenticated):
    """
    Permission class for goal's group leaders
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.group.leader


class GoalPermission(permissions.IsAuthenticated):
    """
    Permission class for goal
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        group = obj.group

        if view.action == "retrieve":
            return user == group.leader or user in group.users.all()
        elif view.action in ["update", "partial_update", "destroy"]:
            return user == group.leader

        return False


class DutyPermission(permissions.IsAuthenticated):
    """
    Permission class for duty
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj.user


class ReportPermission(permissions.IsAuthenticated):
    """
    Permission class for report
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        group = obj.goal.group

        if view.action == "retrieve":
            return user == group.leader or user in group.users.all()
        elif view.action in ["update", "partial_update", "destroy"]:
            return user == group.leader

        return False


class EventPermission(permissions.IsAuthenticated):
    """
    Permission class for event
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        group = obj.group
        if obj.goal is not None:
            group = obj.goal.group

        if group is None:
            return True

        return user == group.leader or user in group.users.all()


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
