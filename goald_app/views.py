# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .models import User

from bcrypt import gensalt, hashpw


def index(request):
	return HttpResponse("Hello bober!")


def login(request):
	return render(request, "login.html", { "form_action" : "auth" })


def register(request):
	return render(request, "register.html", { "form_action" : "create" })


def auth(request):
	if not request.POST:
		return redirect("login", request)

	if not "login" in request.POST or not "password" in request.POST:
		return redirect("login", request)

	user = None
	try:
		user = User.objects.get(name=request.POST["login"])
	except User.DoesNotExist:
		messages.error(request, "Incorrect login or password!")
		return redirect("login")

	salted_hash = hashpw(bytes(request.POST["password"], "utf-8"), user.salt)

	if salted_hash != user.password:
		messages.error(request, "Incorrect login or password!")
		return redirect("login")

	request.session['authorized_as'] = request.POST["login"]
	return redirect("users")


def create(request):
	if not request.POST:
		return redirect("register")

	if not "login" in request.POST or not "password" in request.POST or not "password_repeat" in request.POST:
		return redirect("register")

	if request.POST["password"] != request.POST["password_repeat"]:
		messages.error(request, "Passwords dont match!")
		return redirect("register")

	if User.objects.filter(name=request.POST["login"]).exists():
		messages.error(request, "User already exists!")
		return redirect("register")

	salt = gensalt()
	salted_hash = hashpw(bytes(request.POST["password"], "utf-8"), salt)

	User.objects.create(name=request.POST["login"], password=salted_hash, salt=salt)

	return redirect("login")


def change(request):
	if not 'authorized_as' in request.session or not request.session['authorized_as']:
		return redirect("login")

	if not User.objects.filter(name=request.session['authorized_as']).exists():
		messages.error(request, "You are not authorized!")
		return redirect("login")

	if not request.POST:	
		return redirect("home")

	user = User.objects.get(name=request.session['authorized_as'])
	user.password = request.POST['password']
	user.save()

	return redirect("home")


def delete(request):
	if not 'authorized_as' in request.session or not request.session['authorized_as']:
		return redirect("login")

	if not User.objects.filter(name=request.session['authorized_as']).exists():
		messages.error(request, "You are not authorized!")
		return redirect("login")

	User.objects.filter(name=request.session['authorized_as']).delete()

	return redirect("login")

def users(request):
	if not 'authorized_as' in request.session or not request.session['authorized_as']:
		return redirect("login")

	return render(request, "users.html", {"users" : User.objects.all()})


def home(request):
	return render()
