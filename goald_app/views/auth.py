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
        """
        Register proc
        """

        user = auth.models.User.objects.create_user(
            username=request.data["username"], 
            password=request.data["password"]
        )
        if user is None:
            return Response(
                data={"detail": "Could not create user"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data={"detail": "OK"},
            status=status.HTTP_200_OK
        )

    @action(methods=["post"], detail=False, permission_classes=[NotAuthenticated])
    def login(self, request):
        """
        Login proc
        """

        username = request.data["username"]
        password = request.data["password"]

        user = auth.authenticate(request, username=username, password=password)

        if user is None:
            return Response(
                data={"detail": "Invalid credentials"},
                status=status.HTTP_400_BAD_REQUEST
            )

        auth.login(request, user)
        return Response(
            data={"detail": "OK"},
            status=status.HTTP_200_OK
        )

    @action(methods=["post"], detail=False)
    def logout(self, request):
        """
        Logout proc
        """

        auth.logout(request._request)
        return Response(
            data={"detail": "OK"},
            status=status.HTTP_200_OK
        )
    