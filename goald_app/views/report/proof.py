'''
File for defining handlers for group.image in Django notation
'''

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.report import ReportManager
from goald_app.managers.image import ImageManager


def update_proof(request, report_id):
    '''
    Handler to update a proof
    '''
    result_report = ReportManager.get(report_id=report_id)
    if not result_report.succeed:
        messages.error(request, result_report.message)
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST" and request.FILES.get("proof"):
        ReportManager.proof(report_id=report_id, text=request.FILES["proof"])
        return redirect("reports")

    return render(request, "reports.html", {"error": "Unable to upload an image"})