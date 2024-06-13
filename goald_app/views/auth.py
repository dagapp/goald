"""
File for defining handlers for group in Django notation
"""

from django.contrib import auth

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from ..serializers import AuthSerializer
from ..permissions import NotAuthenticated

class AuthViewSet(viewsets.GenericViewSet):
    """
    GenericViewSet for a auth
    """

    serializer_class = AuthSerializer

    @action(methods=["post"], detail=False, permission_classes=[NotAuthenticated])
    def register(self, request):
        user = auth.models.User.objects.create_user(username=request.data["username"], password=request.data["password"])
        if user is None:
            return Response(
                data={"detail": "Could not create user"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            return Response(
                data={"detail": "OK"},
                status=status.HTTP_200_OK
            )

    @action(methods=["post"], detail=False, permission_classes=[NotAuthenticated])
    def login(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = auth.authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                data={"detail": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            auth.login(request, user)
            return Response(
                data={"detail": "OK"},
                status=status.HTTP_200_OK
            )

    @action(methods=["post"], detail=False)
    def logout(self, request):
        auth.logout(request._request) #Extracts django.http.HttpRequest from rest_framework.request.Request
        return Response(
            data={"detail": "OK"},
            status=status.HTTP_200_OK
        )