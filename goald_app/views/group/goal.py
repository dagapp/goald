"""
File for defining handlers for group in Django notation
"""

import json

from django.http import JsonResponse

from goald_app.managers.common import AlreadyExists, DoesNotExist
from goald_app.managers.goal import GoalManager


def add(request, group_id):
    """
    Handler to add a goal to a group
    """
    if not request.POST:
        return JsonResponse({"Result": "Bad", "msg": "not POST"})

    data = json.loads(request.body)
    if not "name" in data:
        return JsonResponse({"Result": "Bad", "msg": "name does not exist in request"})

    try:
        GoalManager.create(name=data["name"], group_id=group_id)
    except DoesNotExist:
        return JsonResponse({"Result": "Bad", "msg": "Group doesn't exist"})
    except AlreadyExists:
        return JsonResponse({"Result": "Bad", "msg": "Goal already exists"})

    return JsonResponse({"Result": "Ok"})
