"""
File for defining handlers for group in Django notation
"""


from django.contrib import messages
from django.shortcuts import render, redirect
from goald_app.managers.common import AlreadyExists

from goald_app.managers.group import GroupManager
from goald_app.managers.image import ImageManager
from django.http import JsonResponse
import json


def create(request):
    """
    Handler to create group
    """
    if not request.POST:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "not POST"}
            )

    data = json.loads(request.body)

    if not "group_name" in data or not "privacy_mode" in data:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "group_name or privacy_mode does not exist in request"}
            )

    image_path = "group/default.jpg"
    if data["group_avatar"] != "":
        image_path = ImageManager.store(request.FILES["group_avatar"])

    selected_privacy_mode = data["privacy_mode"]
    is_public = False
    if selected_privacy_mode == "public":
        is_public = True

    try:
        GroupManager.create(
            name=data["group_name"],
            image=image_path,
            leader_id=request.session["id"],
            is_public=is_public,
        )
    except AlreadyExists:
        return JsonResponse(
            {"Result" : "Bad", 
            "msg": "group already exists"}
            )

    return JsonResponse({"Result" : "Ok"})


def view(request, group_id):
    """
    Handler to serialize group to json
    """
    group = GroupManager.get(group_id=group_id)

    return JsonResponse({
        "group": {
            "name": group.name,
            "tag": group.tag,
            "is_public": group.is_public,
            "image": group.image.url,
            "users": [ {"login": user.login} for user in group.users.all() ],
            "leader_login": group.leader.login,
        },
        "goals": [goal.name for goal in group.goals_group.all()],
        "events": [event.name for event in group.events_group.all()],
    })

def list(request):
    """
    Handler to serialize groups to json
    """
    groups = GroupManager.get_all_by_user_id(user_id=request.session['id'])
    result = []
    for group in groups:
        result.append({
            "id": group.id,
            "name": group.name,
            "tag": group.tag,
            "image": group.image.url,
        })

    return JsonResponse(result, safe=False)
