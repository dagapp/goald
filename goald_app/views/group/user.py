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

    data = json.loads(request.POST["data"])

    if "tag" not in data:
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": "group_id parameter does not exist in the POST request"
            })

    group_tag = data["tag"]
    try:
        Manager.add_user_to_group(group_tag=group_tag, user_id=request.session["id"])
    except DoesNotExist as e:
        return JsonResponse(
            {
                "Result": "Bad request",
                "msg": f"Failed to add user: {e}"
            })

    return JsonResponse({"Result": "Ok"})
