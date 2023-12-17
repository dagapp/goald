'''
File for defining handlers for group in Django notation
'''

import os

from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from goald_app.managers.group import GroupManager


def create(request):
    '''
    Handler to create group
    '''
    if not request.POST:
        return redirect("home")

    if not "group_name" in request.POST or not "privacy_mode" in request.POST:
        return redirect("home")

    image_path = "static/images/groupProfiles/wNHQWT4wufY.jpg"
    if request.POST.get("group_avatar", None) != "":
        image = request.FILES["group_avatar"]

        storage_location = os.path.join(
            settings.BASE_DIR, "goald_app", "static", "images", "groupProfiles"
        )
        fs = FileSystemStorage(location=storage_location)
        fs.save(image.name, image)
        image_path = "static/images/groupProfiles/" + image.name

    selected_privacy_mode = request.POST.get("privacy_mode", None)
    is_public = False
    if selected_privacy_mode == "public":
        is_public = True

    result = GroupManager.create(
        leader_id=request.session["id"],
        name=request.POST["group_name"],
        image=image_path,
        is_public=is_public,
    )
    if not result.succeed:
        messages.error(request, result.message)

    return redirect("home")


def view(request, group_id):
    '''
    Handler of a group page
    '''
    # Check if request has needed session_id cookie
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    result = GroupManager.objects_get(group_id=group_id)
    if not result.succeed:
        messages.error(request, result.message)
        return redirect("home")

    return render(request, "group_detail.html", {"group": result.result})
