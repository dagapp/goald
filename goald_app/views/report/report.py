'''
File for defining handlers for group in Django notation
'''


from django.contrib import messages
from django.shortcuts import render, redirect

from goald_app.managers.report import ReportManager
from goald_app.managers.image import ImageManager

def create(request, goal_id: int):
    '''
    Handler to create report
    '''
    if not request.POST:
        return redirect("home")

    if not "report_text" in request.POST or not "report_proof" in request.POST:
        return redirect("home")

    proof = ImageManager.store(request.FILES["report_proof"]).result

    result = ReportManager.create(
        goal_id=goal_id,
        text=request.POST["report_text"],
        proof=proof
    )
    if not result.succeed:
        messages.error(request, result.message)

    return redirect("goal")