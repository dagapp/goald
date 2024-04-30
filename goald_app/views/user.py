"""
File for defining handlers for group in Django notation
"""

from bcrypt import gensalt, hashpw, checkpw

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from ..models import User
from ..serializers import UserSerializer, UserLoginSerializer


@api_view(["POST"])
def login(request):
    """
    Handler for logging in a user
    """

    user_login = UserLoginSerializer(data=request.data)

    if not user_login.is_valid():
        return Response(
            data={"detail": "User data is not valid"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if not User.objects.filter(login=user_login.initial_data["login"]).exists():
        return Response(
            data={"detail": "User does not exist"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User.objects.get(login=user_login.initial_data["login"])

    if not checkpw(user_login.initial_data["password"].encode(), user.password):
        return Response(
            data={"detail": "Wrong password"},
            status=status.HTTP_400_BAD_REQUEST
        )

    request.session["id"] = user.id

    return Response(
        data={"detail": "OK"},
        status=status.HTTP_200_OK
    )

@api_view(["POST"])
def logout(request):
    """
    Handler for logging out a user
    """
    
    request.session.flush()

    return Response(
        data={"detail": "OK"},
        status=status.HTTP_200_OK
    )


class UserView(APIView):
    """
        Description of UserView
    """
    def get(self, request):
        """
        Handler for reading the user info
        """

        user = User.objects.get(id=request.session["id"])
        return Response(
            data=UserSerializer(instance=user).data,
            status=status.HTTP_200_OK
        )


    def post(self, request):
        """
        Handler for creating a user
        """

        user = UserSerializer(data=request.data)

        if User.objects.filter(login=request.data["login"]).exists():
            raise serializers.ValidationError("User with this login already exists")

        if not user.is_valid():
            return Response(
                data={"detail": "User data is not valid"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.password = hashpw(bytes(user.password, "utf-8"), gensalt())

        user.save()
        return Response(
            data={"detail", f"User id: {user.data['id']}"},
            status=status.HTTP_201_CREATED
        )

    def patch(self, request):
        """
        Handler for updating the user info
        """

        user = UserSerializer(data=request.data)
        
        if not user.is_valid():
            return Response(
                data={"detail": "User data is not valid"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        User.objects.get(id=request.session["id"]).update(user)

        return Response(
            data={"detail": "User info updated"},
            status=status.HTTP_200_OK
        )


    def delete(self, request):
        """
        Handler for deleting the user
        """

        User.objects.filter(id=request.session["id"]).delete()

        request.session.flush()

        return Response(
            data={"detail": "User deleted"},
            status=status.HTTP_200_OK
        )
