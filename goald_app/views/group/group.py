"""
File for defining handlers for group in Django notation
"""


from django.contrib import messages
from django.shortcuts import render, redirect
from goald_app.managers.common import AlreadyExists

from goald_app.managers.group import GroupManager
from goald_app.managers.image import ImageManager
from django.http import JsonResponse


def create(request):
    """
    Handler to create group
    """
    if not request.POST:
        return redirect("home")

    if not "group_name" in request.POST or not "privacy_mode" in request.POST:
        return redirect("home")

    image_path = "group/default.jpg"
    if request.POST.get("group_avatar", None) != "":
        image_path = ImageManager.store(request.FILES["group_avatar"])

    selected_privacy_mode = request.POST.get("privacy_mode", None)
    is_public = False
    if selected_privacy_mode == "public":
        is_public = True

    try:
        GroupManager.create(
            name=request.POST["group_name"],
            image=image_path,
            leader_id=request.session["id"],
            is_public=is_public,
        )
    except AlreadyExists:
        messages.error(request, "Group already exists")

    return redirect("home")


def view(request, group_id):
    """
    Handler to serialize group to json
    """
    result = {}
    group = GroupManager.get(group_id=group_id)
    result['name'] = group.name
    result['tag'] = group.tag
    result['is_public'] = group.is_public
    result['image'] = group.image.url
    result['users'] = [ {'login': user.login} for user in group.users.all() ]
    result['leader_login'] = group.leader.login
    result['goals'] = [goal.name for goal in group.goals_group.all()]
    result['events'] = [event.name for event in group.events_group.all()]

    return JsonResponse(result)

def list(user_id: int):
    """
    Handler to serialize groups to json
    """
    groups = GroupManager.get_all_by_user_id(user_id=user_id)
    result = []
    grp = {}
    for group in groups:
        grp['name'] = group.name
        grp['tag'] = group.tag
        grp['image'] = group.image
        result.append(grp)

    return JsonResponse(result)
