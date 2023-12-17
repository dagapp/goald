"""
File for defining handlers for group.image in Django notation
"""

from django.contrib import messages
from django.shortcuts import redirect

from goald_app.managers.common import DoesNotExist
from goald_app.managers.report import ReportManager


def update(request, report_id):
    """
    Handler to update a text
    """
    if request.method == "POST" and request.FILES.get("proof"):
        try:
            ReportManager.text(report_id=report_id, text=request.FILES["text"])
        except DoesNotExist:
            messages.error(request, "Report doesn't exist")
    else:
        messages.error(request, "Wrong HTTP method for updating the text")

    return redirect(request.META.get("HTTP_REFERER"))
