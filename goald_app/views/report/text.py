'''
File for defining handlers for group.image in Django notation
'''

from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.report import ReportManager


def update_text(request, report_id):
    '''
    Handler to update a text
    '''
    result_report = ReportManager.get(report_id=report_id)
    if not result_report.succeed:
        messages.error(request, result_report.message)
        return redirect(request.META.get("HTTP_REFERER"))

    if request.method == "POST" and request.FILES.get("text"):
        ReportManager.text(report_id=report_id, text=request.FILES["text"])
        return redirect("reports")

    return render(request, "reports.html", {"error": "Unable to upload an text"})