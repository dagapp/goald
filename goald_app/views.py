'''
File for defining handlers in Django notation
'''

import os

from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from goald_app.managers.manager import AuthManager
from goald_app.managers.user import UserManager
from goald_app.managers.duty import DutyManager
from goald_app.managers.goal import GoalManager
from goald_app.managers.group import GroupManager


def index(request):
    '''
    Main page of the app
    '''
    return HttpResponse("Hello bober!")


def home(request):
    '''
    Home page of the app
    '''
    return render(request, "home.html", {"groups": GroupManager.objects_all().result})


def login(request):
    '''
    Handler to login a user
    '''
    return render(request, "login.html", {"form_action": "auth"})


def register(request):
    '''
    Handler to register a user
    '''
    return render(request, "register.html", {"form_action": "create"})


def user_create(request):
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


def user_auth(request):
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
    request.session["id"] = UserManager.objects_get(user_login).result.id

    return redirect("users")


def user_deauth(request):
    '''
    Handler to deauth the user
    '''
    if "id" not in request.session or not request.session["id"]:
        return redirect("login")

    # Deleting session
    request.session.pop("id")

    return redirect("login")


def user_change(request):
    '''
    Handler to change the password
    '''
    # Check if request has needed session_id cookie,
    # if user actually exists,
    # if request is POST
    # if it has password field
    if "id" not in request.session or not request.session["id"]:
        return redirect("login")

    result = UserManager.exists(request.session["id"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("login")

    if not request.POST:
        return redirect("home")

    if "password" not in request.POST:
        return redirect("home")

    # Call UserManager.change to change user"s password
    result = UserManager.change(request.session["id"], request.POST["password"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("home")

    return redirect("home")


def user_delete(request):
    '''
    Handler to delete the user
    '''
    # Check if request has needed session_id cookie,
    # if user actually exists
    if "id" not in request.session or not request.session["id"]:
        return redirect("login")

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


def test_users(request):
    '''
    Handler to get all users from database
    '''
    # Check if request has needed session_id cookie
    if "id" not in request.session or not request.session["id"]:
        return redirect("login")

    return render(request, "users.html", {"users": UserManager.objects_all().result})


def test_goals(request):
    '''
    Handler to get goals of a user
    '''
    # Check if request has needed session_id cookie,
    # if request is GET,
    # if it has id field
    if "id" not in request.session or not request.session["id"]:
        return redirect("home")

    AuthManager.auth(request.session["id"])

    if request.GET:
        if "goal_id" not in request.GET:
            return redirect("home")

        result = GoalManager.objects_get(goal_id=request.GET["goal_id"])
        if not result.succeed:
            messages.error(request, result.message)
            return redirect("home")

        return render(request, "goals.html", {"goals": result.result})

    result = GoalManager.objects_all()
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("home")

    return render(request, "goals.html", {"goals": result.result})


def test_duties(request):
    '''
    Handler to get all duties
    '''
    # Check if request has needed session_id cookie
    if "id" not in request.session or not request.session["id"]:
        return redirect("login")

    return render(request, "duties.html", {"duties": DutyManager.objects_all()})


def group_create(request):
    '''
    Handler to create group
    '''
    if not request.POST:
        return redirect("home")

    if not "group_name" in request.POST or not "privacy_mode" in request.POST:
        return redirect("home")

    image = request.FILES["group_avatar"]

    storage_location = os.path.join(
        settings.BASE_DIR, "goald_app", "static", "images", "groupProfiles"
    )
    fs = FileSystemStorage(location=storage_location)
    fs.save(image.name, image)
    image_path = "static/images/groupProfiles/" + image.name

    selected_privacy_mode = request.POST.get("privacy_mode", None)
    is_public = False
    if selected_privacy_mode == "public":
        is_public = True

    result = GroupManager.create(
        leader_id=request.session["id"],
        name=request.POST["group_name"],
        image=image_path,
        is_public=is_public,
    )
    if not result.succeed:
        messages.error(request, result.message)

    return redirect("home")


def group(request, group_id):
    '''
    Handler of a group page
    '''
    # Check if request has needed session_id cookie
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    result = GroupManager.objects_get(group_id=group_id)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("home")

    return render(request, "group_detail.html", {"group": result.result})


def group_image_update(request, group_id):
    '''
    Handler to update a group image
    '''
    result = GroupManager.objects_get(group_id=group_id)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        image = request.FILES["group_avatar"]

        storage_location = os.path.join(
            settings.BASE_DIR, "goald_app", "static", "images", "groupProfiles"
        )
        fs = FileSystemStorage(location=storage_location)
        fs.save(image.name, image)
        image_path = "static/images/groupProfiles/" + image.name

        result_group = result.result
        result_group.image = image_path
        result_group.save()

        return render(request, "group_detail.html", {"group": result_group})

    return render(request, "group_detail.html", {"error": "Unable to upload an image"})


def group_user_add(request, group_id):
    '''
    Handler to add a user to a group
    '''
    result = GroupManager.objects_get(group_id=group_id)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST":
        result_group = result.result
        username = request.POST["username"]

        get_user = UserManager.objects_get(login=username)
        if not get_user.succeed:
            messages.error(request, get_user.message)
            return redirect(request.META.get("HTTP_REFERER"))

        result_group.users.add(get_user.result)
        result_group.save()

        return render(request, "group_detail.html", {"group": result_group})

    return render(request, "group_detail.html", {"error": "Unable to add a user"})


def group_goal_add(request, group_id):
    '''
    Handler to add a goal to a group
    '''
    if not request.POST:
        return redirect(request.META.get("HTTP_REFERER"))

    if not "name" in request.POST:
        return redirect(request.META.get("HTTP_REFERER"))

    result = GoalManager.create(name=request.POST["name"], group_id=group_id)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect(request.META.get("HTTP_REFERER"))

    return render(
        request,
        "group_detail.html",
        {"group": GroupManager.objects_get(group_id=group_id).result},
    )
