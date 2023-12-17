"""
File for defining handlers for common pages in Django notation
"""

from django.shortcuts import render, redirect

from goald_app.managers.group import GroupManager


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
    return render(request, "login.html", {"form_action": "user/auth"})


def register(request):
    """
    Handler for registering a user
    """
    return render(request, "register.html", {"form_action": "user/create"})


def logout(request):
    """
    Handler for logging out a user
    """
    return redirect("login")
