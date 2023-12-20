"""
File for defining handlers for group.image in Django notation
"""

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.manager.manager import Manager


def update(request, group_id):
    """
    Handler to update a group image
    """
    if not Manager.group_exists(group_id=group_id):
        messages.error(request, f"Group with such id [{group_id}] doesn't exist")
        return redirect(request.META.get("HTTP_REFERER"))

    group = Manager.get_group(group_id=group_id)

    image_file = request.FILES.get("image")
    if request.method == "POST" and image_file is not None:
        group_avatar = request.FILES["group_avatar"]
        image = Manager.store_image(img=group_avatar)

        group.image = image
        group.save()

        return render(request, "group.html", {"group": group})

    return render(request, "group.html", {"error": "Unable to upload an image"})
