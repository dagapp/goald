"""
File for defining handlers for group in Django notation
"""

import json

from django.http import JsonResponse

from goald_app.managers.common import AlreadyExists
from goald_app.managers.group import GroupManager
from goald_app.managers.image import ImageManager


def create(request):
    """
    Handler to create group
    """
    if not request.POST:
        return JsonResponse({
            "result" : "error", 
            "message": "wrong HTTP method"
        })

    data = json.loads(request.body)

    if not "name" in data or not "is_private" in data:
        return JsonResponse({
            "result" : "error", 
            "message": "group_name or privacy_mode doesn't exist in request"
        })

    image_path = "group/default.jpg"
    if data["image"] != "":
        image_path = ImageManager.store(request.FILES["image"])

    selected_privacy_mode = data["is_private"]
    is_public = False
    if selected_privacy_mode == "public":
        is_public = True

    try:
        GroupManager.create(
            name=data["name"],
            image=image_path,
            leader_id=request.session["id"],
            is_public=is_public,
        )
    except AlreadyExists:
        return JsonResponse({
            "result" : "error", 
            "message": "group already exists"
        })

    return JsonResponse({"result" : "ok"})


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
