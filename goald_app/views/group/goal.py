'''
File for defining handlers for group in Django notation
'''

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.goal import GoalManager
from goald_app.managers.group import GroupManager


def add(request, group_id):
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
        {"group": GroupManager.get(group_id=group_id).result},
    )
