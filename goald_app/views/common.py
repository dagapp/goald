'''
File for defining handlers for common pages in Django notation
'''

from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request, "home.html", {"groups": GroupManager.get_all_by_user_id(request.session["id"]).result})


def login(request):
    '''
    Handler to login a user
    '''
    return render(request, "login.html", {"form_action": "user/auth"})


def register(request):
    '''
    Handler to register a user
    '''
    return render(request, "register.html", {"form_action": "user/create"})
