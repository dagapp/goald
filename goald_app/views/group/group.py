"""
File for defining handlers for group in Django notation
"""
import json

from django.http import JsonResponse

from goald_app.manager.exceptions import AlreadyExists
from goald_app.manager.manager import Manager, DataclassEncoder


def create(request):
    """
    Handler to create group
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "result": "Bad request",
                "message": "wrong HTTP method, expected POST"
            })

    data = json.loads(request.body)

    if "name" not in data or "is_private" not in data:
        return JsonResponse(
            {
                "result": "Bad",
                "message": "group_name or privacy_mode parameter doesn't exist in the request"
            })

    image_path = "group/default.jpg"

    if data["image"] != "":
        image_file = request.FILES["image"]
        image_path = Manager.store_image(image=image_file)

    selected_privacy_mode = data["is_private"]
    is_public = False
    if selected_privacy_mode == "public":
        is_public = True

    try:
        Manager.create_group(
            name=data["name"],
            image=image_path,
            leader_id=request.session["id"],
            is_public=is_public,
        )
    except AlreadyExists as e:
        return JsonResponse(
            {
                "result": "Bad",
                "message": f"Failed to create a group: {e}"
            })

    return JsonResponse({"result": "Ok"})


def view(request, group_id):
    """
    Handler to serialize group to json
    """
    group = Manager.get_user_group(user_id=request.session['id'], group_id=group_id)
    return JsonResponse(data=group, safe=False, encoder=DataclassEncoder)


def list(request):
    """
    Handler to serialize groups to json
    """
    groups = Manager.get_user_groups(user_id=request.session['id'])
    return JsonResponse(data=groups, safe=False, encoder=DataclassEncoder)
