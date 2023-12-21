"""
File for defining handlers for group in Django notation
"""
from django.http import JsonResponse
from django.shortcuts import redirect

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager



def change(request):
    """
    Handler to change the password
    """
    if not request.method == "POST":
        return redirect("home")

    if "password" not in request.POST:
        return redirect("home")

    # Call UserManager.change to change user"s password
    Manager.user_change_password(
        request.session["id"], request.POST["password"]
    )

    return redirect("home")


def delete(request):
    """
    Handler to delete the user
    """
    # Call Manager.delete to find and delete a user
    Manager.delete_user(request.session["id"])

    # Deleting session
    request.session.pop("id")

    return redirect("login")


def summary(request):
    """
    Handler to get all goals for user in json format
    """
    try:
        goals = Manager.get_user_goals(user_id=request.session["id"])
    except DoesNotExist:
        return JsonResponse(
            {
                "goals": [],
                "events": [],
            })

    return JsonResponse(
        {
            "goals": [
                {
                    "name": goal.name,
                } for goal in goals
            ],
            "events": [],
        })
