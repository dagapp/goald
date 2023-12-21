"""
File for defining handlers for group.image in Django notation
"""
from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager


def update(request, group_id):
    """
    Handler to update a group image
    """
    user_id = request.session["id"]
    try:
        group = Manager.get_user_group(user_id=user_id, group_id=group_id)
    except DoesNotExist:
        messages.error(request, f"Group with such id [{group_id}] doesn't exist")
        return redirect(request.META.get("HTTP_REFERER"))

    image_file = request.FILES.get("image")
    if request.method == "POST" and image_file is not None:
        group_avatar = request.FILES["group_avatar"]
        image = Manager.store_image(image=group_avatar)

        Manager.update_group_image(group_id=group_id, image=image)

        return render(request, "group.html", {"group": group})

    return render(request, "group.html", {"error": "Unable to upload an image"})
