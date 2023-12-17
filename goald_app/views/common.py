"""
File for defining handlers for common pages in Django notation
"""

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.common import IncorrectData, DoesNotExist, AlreadyExists
from goald_app.managers.group import GroupManager
from goald_app.managers.user import UserManager


def home(request):
    """
    Handler for home page of the app
    """
    return render(
        request,
        "home.html",
        {"groups": GroupManager.get_all_by_user_id(request.session["id"])},
    )


def login(request):
    """
    Handler for logging in a user
    """
    # either request for login page or passing params
    # depends on type of request
    if request.method == "GET":
        return render(request, "login.html", {"form_action": "login"})

    assert request.method == "POST"

    if "login" not in request.POST or "password" not in request.POST:
        return redirect("login")

    # Call UserManager.auth to authenticate a user
    user_login = request.POST["login"]
    user_password = request.POST["password"]

    try:
        UserManager.auth(user_login, user_password)

    except (DoesNotExist, IncorrectData):
        messages.error(request, "Incorrect login or password")
        return redirect("login")

    # Set a session for further user authorizing
    request.session["id"] = UserManager.get(user_login).id

    return redirect("home")


def register(request):
    """
    Handler for registering a user
    """
    # either request for login page or passing params
    # depends on type of request
    if request.method == "GET":
        return render(request, "register.html", {"form_action": "register"})

    assert request.method == "POST"

    if (
        "login" not in request.POST
        or "password" not in request.POST
        or "password_repeat" not in request.POST
    ):
        return redirect("register")

    if request.POST["password"] != request.POST["password_repeat"]:
        messages.error(request, "Passwords dont match!")
        return redirect("register")

    # Call UserManager.create to create a user
    try:
        UserManager.create(request.POST["login"], request.POST["password"])
    except AlreadyExists:
        messages.error(request, "User with such login already exists")
        return redirect("register")

    return redirect("login")


def logout(request):
    """
    Handler for logging out a user
    """
    # Deleting session
    request.session.pop("id")

    return redirect("login")
