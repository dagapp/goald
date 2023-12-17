"""
File for defining handlers for group in Django notation
"""

from django.contrib import messages
from django.shortcuts import render, redirect
from goald_app.managers.common import AlreadyExists, DoesNotExist

from goald_app.managers.goal import GoalManager
from goald_app.managers.group import GroupManager


def add(request, group_id):
    """
    Handler to add a goal to a group
    """
    if not request.POST:
        return redirect(request.META.get("HTTP_REFERER"))

    if not "name" in request.POST:
        return redirect(request.META.get("HTTP_REFERER"))

    try:
        GoalManager.create(name=request.POST["name"], group_id=group_id)
    except DoesNotExist:
        messages.error(request, "Group doesn't exist")
        return redirect(request.META.get("HTTP_REFERER"))
    except AlreadyExists:
        messages.error(request, "Goal already exists")
        return redirect(request.META.get("HTTP_REFERER"))

    return render(
        request,
        "group.html",
        {"group": GroupManager.get(group_id=group_id)},
    )
