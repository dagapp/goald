"""
File for defining handlers for group.image in Django notation
"""

from django.contrib import messages
from django.shortcuts import redirect

from goald_app.manager.manager import Manager
from goald_app.manager.exceptions import DoesNotExist


def update(request, report_id):
    """
    Handler to update a proof
    """
    proof = request.FILES["proof"]

    if request.method == "POST" and proof is not None:
        try:
            Manager.update_proof(report_id=report_id, proof=proof)
        except DoesNotExist as e:
            messages.error(request, e)
    else:
        messages.error(request, "Wrong HTTP method, expected POST")

    return redirect(request.META.get("HTTP_REFERER"))
