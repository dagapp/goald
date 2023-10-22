# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .models import User

def index(request):
	return HttpResponse("Hello bober!")


def login(request):
	return render(request, "login.html")


def register(request):
	return render(request, "register.html")


def auth(request):
	if not request.POST:
		return redirect("login", request)

	if User.objects.filter(name=request.POST["login"], password=request.POST["password"]).exists():
		return redirect("users")

	messages.error(request, "Incorrect login or password!")
	return redirect("login")


def create(request):
	if not request.POST:
		return redirect("register")

	if request.POST["password"] != request.POST["password_repeat"]:
		messages.error(request, "Passwords dont match!")
		return redirect("register")

	User.objects.create(name=request.POST["login"], password=request.POST["password"])

	return redirect("login")


def users(request):
	return render(request, "users.html", {"users" : User.objects.all()})