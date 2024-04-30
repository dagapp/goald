"""
File for defining handlers for group in Django notation
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from ..models import User, Group
from ..serializers import GroupSerializer


class GroupView(APIView):
    """
       Description of GroupView
    """

    def get(self, request, **kwargs):
        """
        Handler for reading the group info
        """

        if "id" not in kwargs:
            return Response(
                data={"detail": "No id given"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Group.objects.filter(id=kwargs["id"]).exists():
            return Response(
                data={"detail": "Group does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        if not User.objects.get(id=request.session["id"]).groups.filter(id=kwargs["id"]).exists() \
            and not Group.objects.filter(leader_id=request.session["id"]).exists():
            return Response(
                data={"detail": "You have no permission to have this info"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        group = Group.objects.get(id=kwargs["id"])
        return Response(
            data=GroupSerializer(instance=group).data,
            status=status.HTTP_200_OK
        )


    def post(self, request):
        """
        Handler for creating a group
        """

        group = GroupSerializer(data=request.data)

        if Group.objects.filter(tag=request.data["tag"]).exists():
            raise serializers.ValidationError("Group with this tag already exists")

        if not group.is_valid():
            return Response(
                data={"detail": "Group data is not valid"},
                status=status.HTTP_400_BAD_REQUEST
            )

        group.save()
        return Response(
            data={"detail", f"Group id: {group.data['id']}"},
            status=status.HTTP_201_CREATED
        )


    def patch(self, request, **kwargs):
        """
        Handler for updating the group info
        """

        if "id" not in kwargs:
            return Response(
                data={"detail": "No id given"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not Group.objects.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "group with given id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        if not Group.objects.filter(id=request.GET["id"],leader_id=request.session["id"]).exists():
            return Response(
                data={"detail": "You have no permission to change group info"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        group = GroupSerializer(data=request.data)
        Group.objects.get(id=request.GET["id"], leader_id=request.session["id"]).update(group)

        return Response(
            data={"detail": "Group info updated"},
            status=status.HTTP_200_OK
        )


    def delete(self, request, **kwargs):
        """
        Handler for deleting the group
        """

        if "id" not in kwargs:
            return Response(
                data={"detail": "No id given"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user_id = request.session["id"]
        group_id = request.GET["id"]

        if not User.objects.filter(id=user_id).groups.filter(id=group_id).exists():
            return Response(
                data={"detail": "No group with given id found"},
                status=status.HTTP_404_NOT_FOUND
            )

        User.objects.filter(id=user_id).groups.get(id=group_id).delete()

        return Response(
            data={"detail": "Group deleted"},
            status=status.HTTP_200_OK
        )
