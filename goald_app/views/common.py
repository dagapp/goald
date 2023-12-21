"""
File for defining handlers for common pages in Django notation
"""
from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.manager.exceptions import IncorrectData, DoesNotExist, AlreadyExists
from goald_app.manager.manager import Manager


def home(request):
    """
    Handler for home page of the app
    """
    return render(
        request,
        "home.html",
        {
            "login": Manager.get_user(user_id=request.session["id"]).login,
            "groups": Manager.get_user_groups(request.session["id"])
        },
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
        user_id = Manager.auth_user(user_login, user_password)
    except (DoesNotExist, IncorrectData) as e:
        messages.error(request, e)
        return redirect("login")

    # Set a session for further user authorizing
    request.session["id"] = user_id

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

    try:
        user_login = request.POST["login"]
        user_password = request.POST["password"]

        Manager.create_user(user_login, user_password)
    except AlreadyExists as e:
        messages.error(request, e)
        return redirect("register")

    return redirect("login")


def logout(request):
    """
    Handler for logging out a user
    """
    # Deleting session
    request.session.pop("id")

    return redirect("login")
