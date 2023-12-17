'''
File for defining handlers for group.image in Django notation
'''

import os

from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from goald_app.managers.group import GroupManager


def update(request, group_id):
    '''
    Handler to update a group image
    '''
    result = GroupManager.objects_get(group_id=group_id)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]
        image = request.FILES["group_avatar"]

        storage_location = os.path.join(
            settings.BASE_DIR, "goald_app", "static", "images", "groupProfiles"
        )
        fs = FileSystemStorage(location=storage_location)
        fs.save(image.name, image)
        image_path = "static/images/groupProfiles/" + image.name

        result_group = result.result
        result_group.image = image_path
        result_group.save()

        return render(request, "group_detail.html", {"group": result_group})

    return render(request, "group_detail.html", {"error": "Unable to upload an image"})
