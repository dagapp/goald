"""
File for defining handlers for group in Django notation
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from ..models import User, Group, Goal
from ..serializers import GoalSerializer

class GoalView(APIView):
    """
        Description of GoalView
    """
    def get(self, request, **kwargs):
        """
        Handler for reading the goals/goal info
        """
        if "id" not in kwargs:
            return Response(
                data={"detail": "No group_id given"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not User.objects.get(id=request.session["id"]).groups.filter(id=kwargs["id"]).exists():
            return Response(
                data={"detail": "You have no permission to have this info"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        group = Group.objects.get(id=kwargs["id"])

        if "goal_id" not in kwargs:
            goals = group.goals_group.all()
            return Response(
                data=GoalSerializer(instance=goals, many=True).data,
                status=status.HTTP_200_OK
            )
        
        if not group.goals_group.filter(id=kwargs["goal_id"]).exists():
            return Response(
                data={"detail": "You have no permission to have this info"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        goal = group.goals_group.get(id=kwargs["goal_id"])
        return Response(
            data=GoalSerializer(instance=goal).data,
            status=status.HTTP_200_OK
        )

    def post(self, request, **kwargs):
        """
        Handler for creating a goal
        """
        if "id" not in kwargs:
            return Response(
                data={"detail": "No group_id given"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not Group.objects.filter(group_id=kwargs["id"], leader_id=request.session["id"]).exists():
            return Response(
                data={"detail": "You have no permission to create goal in this group"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        goal = GoalSerializer(data=request.data)
        if Goal.objects.filter(**request.data).exists():
            raise serializers.ValidationError("This goal already exists")

        if not goal.is_valid():
            return Response(
                data={"detail": "Duty data is not valid"},
                status=status.HTTP_400_BAD_REQUEST
            )

        goal.save(group=Group.objects.get(id=kwargs["id"]))
        return Response(
            data={"detail", f"OK. Goal: {goal.data}"},
            status=status.HTTP_201_CREATED
        )
    
    def patch(self, request, **kwargs):
        """
        Handler for patch a goal
        """
        if "id" not in kwargs:
            return Response(
                data={"detail": "No group_id given"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not Group.objects.filter(id=kwargs["id"], leader_id=request.session["id"]).exists():
            return Response(
                data={"detail": "You have no permission to change goal in this group"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if "goal_id" not in kwargs:
            return Response(
                data={"detail": "No goal_id given"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        group = Group.objects.get(id=kwargs["id"])
        if not group.goals_group.filter(id=kwargs["goal_id"]).exists():
            return Response(
                data={"detail": "You have no permission to change this goal"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        instance = Goal.objects.get(id=kwargs["goal_id"])

        serializer = GoalSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={"detail": "Group info updated"},
            status=status.HTTP_200_OK
        )

    def delete(self, request, **kwargs):
        """
        Handler for delete a goal
        """
        if "id" not in kwargs:
            return Response(
                data={"detail": "No group_id given"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if not Group.objects.filter(id=kwargs["id"], leader_id=request.session["id"]).exists():
            return Response(
                data={"detail": "You have no permission to change goal in this group"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        if "goal_id" not in kwargs:
            return Response(
                data={"detail": "No goal_id given"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        group = Group.objects.get(id=kwargs["id"])
        if not group.goals_group.filter(id=kwargs["goal_id"]).exists():
            return Response(
                data={"detail": "You have no permission to change this goal"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        Goal.objects.get(id=kwargs["goal_id"]).delete()

        return Response(
            data={"detail": "Group deleted"},
            status=status.HTTP_200_OK
        )