'''
File for defining handlers for group.image in Django notation
'''

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.group import GroupManager
from goald_app.managers.image import ImageManager


def update(request, group_id):
    '''
    Handler to update a group image
    '''
    result_group = GroupManager.objects_get(group_id=group_id)
    if not result_group.succeed:
        messages.error(request, result_group.message)
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST" and request.FILES.get("image"):
        result_image = ImageManager.store(request.FILES["group_avatar"])

        group = result_group.result
        group.image = result_image.result
        group.save()

        return render(request, "group_detail.html", {"group": group})

    return render(request, "group_detail.html", {"error": "Unable to upload an image"})
