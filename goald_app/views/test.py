'''
File for defining handlers for test in Django notation
'''

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.user import UserManager
from goald_app.managers.duty import DutyManager
from goald_app.managers.goal import GoalManager


def users(request):
    '''
    Handler to get all users from database
    '''
    return render(request, "users.html", {"users" : UserManager.objects_all().result})


def goals(request):
    '''
    Handler to get goals of a user
    '''
    # Check
    # if request is GET,
    # if it has id field
    user_id = request.session["id"]

    if request.GET:
        if "goal_id" not in request.GET:
            return redirect("home")

        result = GoalManager.objects_get(goal_id=request.GET["goal_id"],
                                         user_id=user_id)
        if not result.succeed:
            messages.error(request, result.message)
            return redirect("home")

        return render(request, "goals.html", {"goals": result.result})

    result = GoalManager.objects_all(user_id=user_id)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("home")

    return render(request, "goals.html", {"goals": result.result})


def duties(request):
    '''
    Handler to get all duties
    '''
    return render(request, "duties.html", {"duties": DutyManager.objects_all()})

