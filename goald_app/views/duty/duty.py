"""
File for defining handlers for group in Django notation
"""
import json

from django.http import JsonResponse

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager

def pay(request):
    """
    Handler to pay duty
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "result": "Bad request",
                "message": "wrong HTTP method, expected POST"
            })

    data = json.loads(request.body)

    if "goal_id" not in data or "value" not in data:
        return JsonResponse(
            {
                "result": "Bad",
                "message": "goal_id or value parameter doesn't exist in the request"
            })

    try:
        Manager.pay_duty(
            user_id=request.session["id"],
            goal_id=data["goal_id"],
            value=data["value"]
            )
    except DoesNotExist as e:
        return JsonResponse(
            {
                "result": "Bad",
                "message": f"Failed to pay a duty: {e}"
            })

    return JsonResponse({"result": "Ok"})


def delegate(request):
    """
    Handler to pay duty
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "result": "Bad request",
                "message": "wrong HTTP method, expected POST"
            })

    data = json.loads(request.body)

    if (
       "goal_id" not in data or
       "value" not in data or
       "delegate_id" not in data
       ):
        return JsonResponse(
            {
                "result": "Bad",
                "message": "goal_id or value or delegate_id parameter doesn't exist in the request"
            })

    try:
        Manager.delegate_duty(
            user_id=request.session["id"],
            goal_id=data["goal_id"],
            delegate_id=data["delegate_id"],
            value=data["value"]
            )
    except DoesNotExist as e:
        return JsonResponse(
            {
                "result": "Bad",
                "message": f"Failed to delegate a duty: {e}"
            })

    return JsonResponse({"result": "Ok"})
