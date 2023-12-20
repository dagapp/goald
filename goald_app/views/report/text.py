"""
File for defining handlers for group.image in Django notation
"""

from django.contrib import messages
from django.shortcuts import redirect

from goald_app.manager.manager import Manager
from goald_app.manager.exceptions import DoesNotExist


def update(request, report_id):
    """
    Handler to update a text
    """
    proof = request.FILES["proof"]

    if request.method == "POST" and proof is not None:
        try:
            Manager.report_text(report_id=report_id, text=request.FILES["text"])
        except DoesNotExist as e:
            messages.error(request, e)
    else:
        messages.error(request, "Wrong HTTP method, expected POST")

    return redirect(request.META.get("HTTP_REFERER"))
