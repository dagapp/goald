"""
File for defining handlers for group in Django notation
"""
import json

from django.http import JsonResponse

from goald_app.manager.exceptions import AlreadyExists
from goald_app.manager.manager import Manager


def add(request, group_id):
    """
    Handler to add a goal to a group
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": "Wrong HTTP method, expected POST"
            })

    data = json.loads(request.POST["data"])

    if "name" not in data:
        return JsonResponse(
            {
                "Result": "Bad",
                "msg": "name parameter does not exist in request"
            })

    try:
        Manager.create_goal(name=data["name"], group_id=group_id)
    except AlreadyExists as e:
        return JsonResponse(
            {
                "Result": "Bad",
                "msg": f"Failed to create goal: {e}"}
            )

    return JsonResponse({"Result": "Ok"})
