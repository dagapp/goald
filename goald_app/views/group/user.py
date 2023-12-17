"""
File for defining handlers for group in Django notation
"""

from django.contrib import messages
from django.shortcuts import redirect
from goald_app.managers.common import DoesNotExist

from goald_app.managers.group import GroupManager


def add(request, group_id):
    """
    Handler to add a user to a group
    """
    if request.method == "POST":
        try:
            GroupManager.add_user(group_id=group_id, login=request.POST["username"])
        except DoesNotExist:
            messages.error(request, "Unable to add user")
    else:
        messages.error(request, "Wrong HTTP method")

    return redirect(request.META.get("HTTP_REFERER"))
