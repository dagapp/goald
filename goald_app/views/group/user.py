"""
File for defining handlers for group in Django notation
"""

from goald_app.manager.manager import Manager
from goald_app.manager.exceptions import DoesNotExist

from django.http import JsonResponse
import json

from django.http import JsonResponse

from goald_app.managers.common import DoesNotExist
from goald_app.managers.group import GroupManager


def add(request, group_id):
    """
    Handler to add a user to a group
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": "Wrong HTTP method, expected POST"
            })

    data = json.load(request.body)

    if "user_name" not in data:
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": "user_name parameter does not exist in the POST request"
            })

    login = data["username"]
    try:
        Manager.add_user_to_group(group_id=group_id, login=login)
    except DoesNotExist as e:
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": f"Failed to add user: {e}"
            })

    return JsonResponse({"Result": "Ok"})
