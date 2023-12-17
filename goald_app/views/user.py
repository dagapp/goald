'''
File for defining handlers for user in Django notation
'''

from django.contrib import messages
from django.shortcuts import redirect

from goald_app.managers.user import UserManager


def create(request):
    '''
    Handler to create a user
    '''
    # Check if request is POST,
    # if it has login, password and password_repeat fields,
    # if password equals to password_repeat
    if not request.POST:
        return redirect("register")

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
    result = UserManager.create(request.POST["login"], request.POST["password"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("register")

    return redirect("login")


def auth(request):
    '''
    Handler to auth the user
    '''
    # Check if request is POST and if it has login and password fields
    if not request.POST:
        return redirect("login", request)

    if "login" not in request.POST or "password" not in request.POST:
        return redirect("login", request)

    # Call UserManager.auth to authenticate a user
    user_login = request.POST["login"]
    user_password = request.POST["password"]

    result = UserManager.auth(user_login, user_password)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("login")

    # Set a session for further user authorizing
    request.session["id"] = UserManager.get(user_login).result.id

    return redirect("home")


def deauth(request):
    '''
    Handler to deauth the user
    '''
    # Deleting session
    request.session.pop("id")

    return redirect("login")


def change(request):
    '''
    Handler to change the password
    '''
    # Check
    # if user actually exists,
    # if request is POST
    # if it has password field

    result = UserManager.exists(request.session["id"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("login")

    if not request.POST:
        return redirect("home")

    if "password" not in request.POST:
        return redirect("home")

    # Call UserManager.change to change user"s password
    result = UserManager.change_password(request.session["id"], request.POST["password"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("home")

    return redirect("home")


def delete(request):
    '''
    Handler to delete the user
    '''
    # Check
    # if user actually exists

    # Call UserManager.exists to know if user exists
    result = UserManager.exists(request.session["id"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("login")

    # Call UserManager.delete to find and delete a user
    UserManager.delete(request.session["id"])

    # Deleting session
    request.session.pop("id")

    return redirect("login")
