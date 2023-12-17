"""
File for defining handlers for group.image in Django notation
"""

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.group import GroupManager
from goald_app.managers.image import ImageManager


def update(request, group_id):
    """
    Handler to update a group image
    """
    if not GroupManager.exists(group_id=group_id):
        messages.error(request, "Group doesn't exist")
        return redirect(request.META.get("HTTP_REFERER"))

    group = GroupManager.get(group_id=group_id)

    if request.method == "POST" and request.FILES.get("image"):
        image = ImageManager.store(request.FILES["group_avatar"])

        group.image = image
        group.save()

        return render(request, "group.html", {"group": group})

    return render(request, "group.html", {"error": "Unable to upload an image"})
