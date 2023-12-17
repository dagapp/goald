"""
File for defining handlers for user in Django notation
"""

from django.contrib import messages
from django.shortcuts import redirect

from goald_app.managers.user import UserManager


def change(request):
    """
    Handler to change the password
    """
    # Check
    # if user actually exists,
    # if request is POST
    # if it has password field

    if not UserManager.exists(user_id=request.session["id"]):
        messages.error(request, "User doesn't exist")
        return redirect("login")

    if not request.POST:
        return redirect("home")

    if "password" not in request.POST:
        return redirect("home")

    # Call UserManager.change to change user"s password
    UserManager.change_password(
        request.session["id"], request.POST["password"]
    )

    return redirect("home")


def delete(request):
    """
    Handler to delete the user
    """
    # Check
    # if user actually exists

    # Call UserManager.exists to know if user exists
    if not UserManager.exists(user_id=request.session["id"]):
        messages.error(request, "User doesn't exist")
        return redirect("login")

    # Call UserManager.delete to find and delete a user
    UserManager.delete(request.session["id"])

    # Deleting session
    request.session.pop("id")

    return redirect("login")
