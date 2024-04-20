"""
File for defining handlers for group.image in Django notation
"""

import json

from django.http import JsonResponse

from goald_app.manager.exceptions import DoesNotExist
from goald_app.manager.manager import Manager


def update(request, report_id):
    """
    Handler to update a proof
    """
    if request.method != "POST":
        return JsonResponse({
            "result": "Bad request",
            "message": "Bad HTTP request, expected POST"
        })

    data = json.loads(request.POST["data"])

    image_path = "group/default.jpg"
    if "image" in data:
        image_file = request.FILES["image"]
        image_path = Manager.store_image(image=image_file)

    try:
        Manager.update_report_proof(
            user_id=request.session["id"],
            report_id=report_id,
            proof=image_path
        )
    except DoesNotExist:
        return JsonResponse({
            "result": "Bad",
            "message": "Report does not exist"
        })

    return JsonResponse({
        "result": "Success",
        "message": "Report proof image created successfully"
    })
