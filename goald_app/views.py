# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import os

from .managers.manager import AuthManager
from .managers.user    import UserManager
from .managers.group   import GroupManager
from .managers.duty    import DutyManager
from .managers.goal    import GoalManager


def index(request):
    return HttpResponse("Hello bober!")


def login(request):
    return render(request, "login.html", { "form_action" : "auth" })


def register(request):
    return render(request, "register.html", { "form_action" : "create" })


def create(request):
    # Check if request is POST,
    # if it has login, password and password_repeat fields,
    # if password equals to password_repeat
    if not request.POST:
        return redirect("register")

    if not "login" in request.POST or not "password" in request.POST or not "password_repeat" in request.POST:
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
    # Check if request is POST and if it has login and password fields
    if not request.POST:
        return redirect("login", request)

    if not "login" in request.POST or not "password" in request.POST:
        return redirect("login", request)

    # Call UserManager.auth to authenticate a user
    login    = request.POST["login"]
    password = request.POST["password"]

    result = UserManager.auth(login, password)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("login")

    # Set a session for further user authorizing
    request.session["id"] = UserManager.objects_get(login).result.id

    return redirect("users")


def deauth(request):
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    # Deleting session
    request.session.pop("id")

    return redirect("login")


def change(request):
    # Check if request has needed session_id cookie,
    # if user actually exists,
    # if request is POST
    # if it has password field
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    result = UserManager.exists(request.session["id"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("login")

    if not request.POST:    
        return redirect("home")
    
    if not "password" in request.POST:
        return redirect("home")

    # Call UserManager.change to change user"s password
    result = UserManager.change(request.session["id"], request.POST["password"])
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("home")

    return redirect("home")


def delete(request):
    # Check if request has needed session_id cookie,
    # if user actually exists
    if not "id" in request.session or not request.session["id"]:
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


def users(request):
    # Check if request has needed session_id cookie
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    return render(request, "users.html", { "users" : UserManager.objects_all().result })


def home(request):
    return render(request, "home.html", { "groups" : GroupManager.objects_all().result })

def createGroup(request):
    if not request.POST:
        return redirect("home")

    if not "group_name" in request.POST or not "privacy_mode" in request.POST:
        return redirect("home")

    image = request.FILES['group_avatar']
    
    storage_location = os.path.join(settings.BASE_DIR, 'goald_app','static', 'images', 'groupProfiles')
    fs = FileSystemStorage(location= storage_location)
    filename = fs.save(image.name, image)
    
    image_path= 'static/images/groupProfiles/' + image.name
    selected_privacy_mode = request.POST.get('privacy_mode', None)
    is_public = False
    if selected_privacy_mode == "Публичный":
        is_public = True

    result = GroupManager.create(leader_id=request.session["id"], tag=request.POST["group_name"], image=image_path, is_public=is_public)
    if not result.succeed:
        messages.error(request, result.message)

    return redirect("home")

def goals(request):
    # Check if request has needed session_id cookie,
    # if request is GET,
    # if it has id field
    if not "id" in request.session or not request.session["id"]:
        return redirect("home")
    
    AuthManager.auth(request.session["id"])

    if request.GET:
        if not "goal_id" in request.GET:
            return redirect("home")

        result = GoalManager.objects_get(id=request.GET["goal_id"])
        if not result.succeed:
            messages.error(request, result.message)
            return redirect("home")

        return render(request, "goals.html", {"goals" : result.result})
    
    else:
        result = GoalManager.objects_all()
        if not result.succeed:
            messages.error(request, result.message)
            return redirect("home")
        
        return render(request, "goals.html", {"goals" : result.result})


def duties(request):
    # Check if request has needed session_id cookie
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    return render(request, "duties.html", {"duties" : DutyManager.objects_all()})