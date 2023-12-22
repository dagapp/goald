"""
File for defining handlers for group in Django notation
"""
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager, DataclassEncoder


def create(request, goal_id: int):
    """
    Handler to create report
    """
    if request.method == "POST":
        return redirect("home")

    if "report_text" not in request.POST or "report_proof" not in request.POST:
        return redirect("home")

    report_text = request.POST["report_text"]
    report_proof = request.FILES["report_proof"]

    proof = Manager.store_image(image=report_proof)

    try:
        Manager.create_report(
            goal_id=goal_id, text=report_text, proof=proof
        )
    except DoesNotExist as e:
        messages.error(request, e)

    return redirect("goal")


def view(request, report_id):
    """
    Handler of a reports page
    """
    if request.method != "POST":
        return JsonResponse({
            "result": "Bad request",
            "message": "Bad HTTP request, expected POST"
        })

    try:
        report = Manager.get_report(report_id=report_id)
        return JsonResponse(data=report, safe=False, encoder=DataclassEncoder)
    except DoesNotExist:
        return JsonResponse({
            "result": "Bad",
            "message": "Report doesn't exist"
        })
