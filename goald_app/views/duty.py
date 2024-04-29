"""
File for defining handlers for group in Django notation
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from ..models import User, Duty
from ..serializers import DutySerializer

class DutyView(APIView):
    """
        Description of DutyView
    """
    def get(self, request):
        """
        Handler for reading the duty info
        """

        user_id = request.session["id"]
        duty_id = request.GET["id"]

        if not User.objects.filter(id=user_id).duties.filter(id=duty_id).exists():
            return Response(
                data={"detail": "You have no permission to have this info"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        duty = Duty.objects.get(id=request.GET["id"])
        return Response(
            data=DutySerializer(instance=duty).data,
            status=status.HTTP_200_OK
        )


    def post(self, request):
        """
        Handler for creating a duty
        """

        duty = DutySerializer(data=request.data)

        if Duty.objects.filter(**request.data).exists():
            #TODO: check out how it works and maybe switch "return Response" with it
            raise serializers.ValidationError("This duty already exists")

        if not duty.is_valid():
            return Response(
                data={"detail": "Duty data is not valid"},
                status=status.HTTP_400_BAD_REQUEST
            )

        duty.save()
        return Response(
            data={"detail", f"OK. Duty id: {duty.data['id']}"},
            status=status.HTTP_201_CREATED
        )


    def patch(self, request):
        """
        Handler for updating the duty info
        """

        duty = DutySerializer(data=request.data)

        user_id = request.session["id"]
        duty_id = request.GET["id"]

        if not Duty.objects.filter(id=duty_id).exists():
            return Response(
                data={"detail": "Duty with given id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        if not User.objects.filter(id=user_id).duties.filter(id=duty_id).exists():
            return Response(
                data={"detail": "You have no permission to change group info"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        Duty.objects.get(id=duty_id).update(duty)

        return Response(
            data={"detail": "OK. Group info updated"},
            status=status.HTTP_200_OK
        )


    def delete(self, request):
        """
        Handler for deleting the duty
        """

        if "id" not in request.GET:
            return Response(
                data={"detail": "No duty id given"},
                status=status.HTTP_404_NOT_FOUND
            )

        user_id = request.session["id"]
        duty_id = request.GET["id"]

        if not User.objects.filter(id=user_id).duties.filter(id=duty_id).exists():
            return Response(
                data={"detail": "No duty with given id found"},
                status=status.HTTP_404_NOT_FOUND
            )

        Duty.objects.get(id=duty_id).delete()

        return Response(
            data={"detail": "OK"},
            status=status.HTTP_200_OK
        )
