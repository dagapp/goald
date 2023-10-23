# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .models import User

def index(request):
	return HttpResponse("Hello bober!")


def login(request):
	return render(request, "login.html", { "form_action" : "auth" })


def register(request):
	return render(request, "register.html", { "form_action" : "create" })


def auth(request):
	if not request.POST:
		return redirect("login", request)

	if User.objects.filter(name=request.POST["login"], password=request.POST["password"]).exists():
		request.session['is_authorized'] = True
		return redirect("users")

	request.session['is_authorized'] = False

	messages.error(request, "Incorrect login or password!")
	return redirect("login")


def create(request):
	if not request.POST:
		return redirect("register")

	if request.POST["password"] != request.POST["password_repeat"]:
		messages.error(request, "Passwords dont match!")
		return redirect("register")

	if User.objects.filter(name=request.POST["login"]).exists():
		messages.error(request, "User already exists!")
		return redirect("register")

	User.objects.create(name=request.POST["login"], password=request.POST["password"])

	return redirect("login")


def users(request):
	if not 'is_authorized' in request.session or not request.session['is_authorized']:
		return redirect("login")

	return render(request, "users.html", {"users" : User.objects.all()})


def home(request):
	return render()
