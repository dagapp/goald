"""
File for defining handlers for group in Django notation
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from ..models import User, Duty
from ..serializers import DutySerializer


class DutyView(APIView):
    def get(self, request):
        """
        Handler for reading the duty info
        """
        
        if not User.objects.filter(id=request.session["id"]).duties.filter(id=request.GET["id"]).exists():
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

        if not Duty.objects.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "Duty with given id does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if not User.objects.filter(id=request.session["id"]).duties.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "You have no permission to change group info"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        Duty.objects.get(id=request.GET["id"]).update(duty)

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

        if not User.objects.filter(id=request.session["id"]).duties.filter(id=request.GET["id"]).exists():
            return Response(
                data={"detail": "No duty with given id found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        Duty.objects.get(id=request.GET["id"]).delete()

        return Response(
            data={"detail": "OK"},
            status=status.HTTP_200_OK
        )


def pay(request):
    """
    Handler to pay duty
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "detail": "Bad request",
                "message": "wrong HTTP method, expected POST"
            })

    data = json.loads(request.POST["data"])

    if "goal_id" not in data or "value" not in data:
        return JsonResponse(
            {
                "detail": "Bad",
                "message": "goal_id or value parameter doesn't exist in the request"
            })

    try:
        Manager.pay_duty(
            user_id=request.session["id"],
            goal_id=data["goal_id"],
            value=data["value"]
            )
    except DoesNotExist:
        return JsonResponse(
            {
                "detail": "Bad",
                "message": "Failed to pay a duty"
            })

    return JsonResponse({"detail": "Ok"})


def delegate(request):
    """
    Handler to pay duty
    """
    if request.method != "POST":
        return JsonResponse(
            {
                "detail": "Bad request",
                "message": "wrong HTTP method, expected POST"
            })

    data = json.loads(request.POST["data"])

    if (
       "goal_id" not in data or
       "value" not in data or
       "delegate_id" not in data
       ):
        return JsonResponse(
            {
                "detail": "Bad",
                "message": "goal_id or value or delegate_id parameter doesn't exist in the request"
            })

    try:
        Manager.delegate_duty(
            user_id=request.session["id"],
            goal_id=data["goal_id"],
            delegate_id=data["delegate_id"],
            value=data["value"]
            )
    except DoesNotExist:
        return JsonResponse(
            {
                "detail": "Bad",
                "message": "Failed to delegate a duty"
            })

    return JsonResponse({"detail": "Ok"})
