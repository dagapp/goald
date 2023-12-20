"""
File for defining handlers for group in Django notation
"""

import json

from django.http import JsonResponse

from goald_app.managers.common import AlreadyExists
from goald_app.managers.group import GroupManager
from goald_app.managers.user import UserManager, dataclass_encoder
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
    group = UserManager.get_group(user_id=request.session['id'], group_id=group_id)
    return JsonResponse(data=group, safe=False, encoder=dataclass_encoder)

def list(request):
    """
    Handler to serialize groups to json
    """
    groups = UserManager.get_groups(user_id=request.session['id'])
    return JsonResponse(data=groups, safe=False, encoder=dataclass_encoder)
