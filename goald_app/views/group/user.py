"""
File for defining handlers for group in Django notation
"""

from django.contrib import messages
from django.shortcuts import redirect
from goald_app.managers.common import DoesNotExist

from goald_app.managers.group import GroupManager
from django.http import JsonResponse
import json


def add(request, group_id):
    """
    Handler to add a user to a group
    """
    if not request.POST:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "not POST"}
            )
    data = json.load(request.body)

    if not "user_name" in data:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "user_name does not exist in request"}
            )

    try:
        GroupManager.add_user(group_id=group_id, login=data["username"])
    except DoesNotExist:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "unable to add user"}
            )

    return JsonResponse({"Result" : "Ok"})
