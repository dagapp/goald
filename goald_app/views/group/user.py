'''
File for defining handlers for group in Django notation
'''

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.user import UserManager
from goald_app.managers.group import GroupManager


def add(request, group_id):
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
