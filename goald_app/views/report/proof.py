"""
File for defining handlers for group.image in Django notation
"""

from django.contrib import messages
from django.shortcuts import render, redirect
from goald_app.managers.common import DoesNotExist

from goald_app.managers.report import ReportManager


def update_proof(request, report_id):
    """
    Handler to update a proof
    """
    if request.method == "POST" and request.FILES.get("proof"):
        try:
            ReportManager.proof(report_id=report_id, text=request.FILES["proof"])
            return redirect(request.META.get("HTTP_REFERER"))
        except DoesNotExist:
            messages.error(request, "Report doesn't exist")
            return redirect(request.META.get("HTTP_REFERER"))

    messages.error(request, "Wrong HTTP method")
    return redirect(request.META.get("HTTP_REFERER"))
