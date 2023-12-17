"""
File for defining handlers for group in Django notation
"""

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.common import DoesNotExist
from goald_app.managers.report import ReportManager
from goald_app.managers.image import ImageManager

from goald_app.views.group import goal


def create(request, goal_id: int):
    """
    Handler to create report
    """
    if not request.POST:
        return redirect("home")

    if not "report_text" in request.POST or not "report_proof" in request.POST:
        return redirect("home")

    proof = ImageManager.store(request.FILES["report_proof"])

    try:
        ReportManager.create(
            goal_id=goal_id, text=request.POST["report_text"], proof=proof
        )
    except DoesNotExist:
        messages.error(request, "Goal doesn't exist")

    return redirect("goal")


def view(request, goal_id):
    """
    Handler of a reports page
    """
    # Check if request has needed session_id cookie
    if not "id" in request.session or not request.session["id"]:
        return redirect("login")

    if not ReportManager.exists(goal_id=goal_id):
        messages.error(request, "Goal doesn't exist")
        return redirect(request.META.get("HTTP_REFERER"))

    return render(
        request, "reports.html", {"reports": ReportManager.get_all(goal_id=goal_id)}
    )
