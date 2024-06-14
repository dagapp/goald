"""
File for defining handlers for group in Django notation
"""

from django.db.models import Q

from django.contrib import auth

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from backend.models import PrivateMessage

from ..serializers import PrivateMessageSerializer
from ..permissions import NotAuthenticated

class UserViewSet(viewsets.GenericViewSet):
    """
    GenericViewSet for a auth
    """

    serializer_class = PrivateMessageSerializer

    @action(methods=["get", "post"], detail=True)
    def chat(self, request, pk):
        sender = request.user
        recipient = auth.User.objects.get(pk=pk)

        if request.method == "GET":
            return Response(
                PrivateMessageSerializer(
                    PrivateMessage.objects.filter(
                        (Q(sender=sender) & Q(recipient=recipient)) | (Q(sender=recipient) & Q(recipient=sender))
                    ),
                    many=True
                ).data,
                status=status.HTTP_200_OK
            )

        message = PrivateMessageSerializer(data=request.data)
        if not message.is_valid():
            return Response(
                {"detail": "Incorrect message"},
                status=status.HTTP_400_BAD_REQUEST
            )

        message.sender = sender
        message.recipient = recipient
        message.save()

        return Response(
            {"detail": "OK"},
            status=status.HTTP_200_OK
        )
