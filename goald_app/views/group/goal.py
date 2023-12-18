"""
File for defining handlers for group in Django notation
"""

from django.contrib import messages
from django.shortcuts import render, redirect
from goald_app.managers.common import AlreadyExists, DoesNotExist

from goald_app.managers.goal import GoalManager
from goald_app.managers.group import GroupManager
from django.http import JsonResponse
import json


def add(request, group_id):
    """
    Handler to add a goal to a group
    """
    if not request.POST:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "not POST"}
            )
    
    data = json.loads(request.body)
    if not "name" in data:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "name does not exist in request"}
            )

    try:
        GoalManager.create(name=data["name"], group_id=group_id)
    except DoesNotExist:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "Group doesn't exist"}
            )
    except AlreadyExists:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "Goal already exists"}
            )

    return JsonResponse({"Result" : "Ok"})
