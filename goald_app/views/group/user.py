"""
File for defining handlers for group in Django notation
"""
import json

from django.http import JsonResponse

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager


def add(request):
    """
    Handler to add a user to a group
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": "Wrong HTTP method, expected POST"
            })

    data = json.load(request.POST["data"])

    if "group_id" not in data:
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": "group_id parameter does not exist in the POST request"
            })

    group_id = data["group_id"]
    try:
        Manager.add_user_to_group(group_id=group_id, login=request.session["id"])
    except DoesNotExist as e:
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": f"Failed to add user: {e}"
            })

    return JsonResponse({"Result": "Ok"})
