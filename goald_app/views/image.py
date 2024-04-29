"""
File for defining handlers for group.image in Django notation
"""

import json

from rest_framework.response import Response
from rest_framework import status

from goald_app.manager import Manager
from ..exceptions import DoesNotExist

def image(request, group_id):
    """
    Handler to update a group image
    """
    if not request.method == "POST":
        return Response(
            data={"detail": "Wrong method, use POST"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    data = json.loads(request.POST["data"])

    image_path = "group/default.jpg"
    if "image" in data:
        image_file = request.FILES["image"]
        image_path = Manager.store_image(image=image_file)

    try:
        Manager.update_group_image(
            user_id=request.session["id"],
            group_id=group_id,
            image=image_path
        )
    except DoesNotExist:
        return Response({
            "detail": "Bad",
            "message": "Group does not exist"
        })

    return Response({
        "detail": "Success",
        "message": "Group image created successfully"
    })
