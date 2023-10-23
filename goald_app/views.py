# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .managers.user import User


def index(request):
	return HttpResponse("Hello bober!")


def login(request):
	return render(request, "login.html", { "form_action" : "auth" })


def register(request):
	return render(request, "register.html", { "form_action" : "create" })


def auth(request):
	# Check if request is POST and if it has login and password fields
	if not request.POST:
		return redirect("login", request)

	if not "login" in request.POST or not "password" in request.POST:
		return redirect("login", request)

	# Call User.auth to authenticate a user
	login    = request.POST["login"]
	password = request.POST["password"]

	result = User.auth(login, password)
	if not result.succeed:
		messages.error(request, result.message)
		return redirect("login")

	# Set a session for further user authorizing
	request.session['authorized_as'] = request.POST["login"]

	return redirect("users")


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

	# Call User.create to create a user
	result = User.create(request.POST["login"], request.POST["password"])
	if not result.succeed:
		messages.error(request, result.message)
		return redirect("register")

	return redirect("login")


def change(request):
	# Check if request has needed session_id cookie,
	# if user actually exists,
	# if request is POST
	if not 'authorized_as' in request.session or not request.session['authorized_as']:
		return redirect("login")

	result = User.exists(request.session['authorized_as'])
	if not result.succeed:
		messages.error(request, result.message)
		return redirect("login")

	if not request.POST:	
		return redirect("home")

	# Call User.change to change user's password
	result = User.change(request.POST["login"], request.POST["password"])
	if not result.succeed:
		messages.error(request, result.message)
		return redirect("home")

	return redirect("home")


def delete(request):
	# Check if request has needed session_id cookie,
	# if user actually exists
	if not 'authorized_as' in request.session or not request.session['authorized_as']:
		return redirect("login")

	# Call User.exists to know if user exists
	result = User.exists(request.session['authorized_as'])
	if not result.succeed:
		messages.error(request, result.message)
		return redirect("login")

	# Call User.delete to find and delete a user
	User.delete(request.session['authorized_as'])

	return redirect("login")


def users(request):
	# Check if request has needed session_id cookie
	if not 'authorized_as' in request.session or not request.session['authorized_as']:
		return redirect("login")

	return render(request, "users.html", {"users" : User.objects.all()})


def home(request):
	return render()
