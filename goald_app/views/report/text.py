"""
File for defining handlers for group.image in Django notation
"""

import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager


def update(request, report_id):
    """
    Handler to update a text
    """
    if request.method != "POST":
        return JsonResponse({
            "result": "Bad request",
            "message": "Bad HTTP request, expected POST"
        })
    
    data = json.loads(request.POST["data"])
    
    if "text" not in data:
        return JsonResponse({
            "result": "Bad",
            "message": "No text in request"
        })
    
    text = data["text"]

    try:
        Manager.update_report_text(report_id=report_id, text=text)
    except DoesNotExist:
        return JsonResponse({
            "result": "Bad",
            "message": ""
        })

    return JsonResponse({
        "result": "Success",
        "message": "Report text updated successfully"
    })
