"""
File for defining handlers for group.image in Django notation
"""
from django.contrib import messages
from django.shortcuts import redirect

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager


def update(request, report_id):
    """
    Handler to update a text
    """
    text = request.FILES["text"]

    if request.method == "POST" and text is not None:
        try:
            Manager.update_report_text(report_id=report_id, text=text)
        except DoesNotExist:
            messages.error(request, "report does not exist")
    else:
        messages.error(request, "Wrong HTTP method, expected POST")

    return redirect(request.META.get("HTTP_REFERER"))
