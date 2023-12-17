"""
File for defining handlers for group in Django notation
"""


from django.contrib import messages
from django.shortcuts import render, redirect
from goald_app.managers.common import AlreadyExists, DoesNotExist

from goald_app.managers.group import GroupManager
from goald_app.managers.image import ImageManager


def create(request):
    """
    Handler to create group
    """
    if not request.POST:
        return redirect("home")

    if not "group_name" in request.POST or not "privacy_mode" in request.POST:
        return redirect("home")

    image_path = "group/default.jpg"
    if request.POST.get("group_avatar", None) != "":
        image_path = ImageManager.store(request.FILES["group_avatar"])

    selected_privacy_mode = request.POST.get("privacy_mode", None)
    is_public = False
    if selected_privacy_mode == "public":
        is_public = True

    try:
        GroupManager.create(
            name=request.POST["group_name"],
            image=image_path,
            leader_id=request.session["id"],
            is_public=is_public,
        )
    except AlreadyExists:
        messages.error(request, "Group already exists")

    return redirect("home")


def view(request, group_id):
    """
    Handler of a group page
    """
    # Check if request has needed session_id cookie
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    if not GroupManager.exists(group_id=group_id):
        messages.error(request, "Group doesn't exist")
        return redirect("home")

    return render(request, "group_detail.html", {"group": GroupManager.get(group_id=group_id)})
