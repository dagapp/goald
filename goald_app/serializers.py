"""
File for defining serializer classes
"""

from django.contrib.auth.models import User
from numpy import source
from rest_framework import serializers
#from django.db.models import fields
from .models import Group, Goal, Duty, Event, Report


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User model objects
    """

    class Meta:
        model = User
        fields = ("id", "username")

class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer class for Group model object
    """

    leader = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Group
        fields = ("id", "tag", "is_public", "name", "image", "leader")


class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer class for Goal model object
    """

    #TODO: make that is_active is inavailable on create
    #is_active = serializers.HiddenField(default=True)

    final_value = serializers.ReadOnlyField()
    current_value = serializers.ReadOnlyField()

    class Meta:
        model = Goal
        fields = (
            "id",
            "name",
            "group",
            "is_active",
            "deadline",
            "alert_period",
            "final_value",
            "current_value"
        )

    #TODO: control create based on permissions
    def create(self, validated_data):
        user = self.context['request'].user
        group = Group.objects.get(tag=validated_data.get("group"))

        if user != group.leader:
            return None
        
        goal = Goal.objects.create(**validated_data)
        return goal

    #TODO: control update based on permissions


class DutySerializer(serializers.ModelSerializer):
    """
    Serializer class for Duty model object
    """

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    current_value = serializers.HiddenField(default=0)

    class Meta:
        model = Duty
        fields = ("id", "user", "goal", "final_value", "current_value", "deadline", "alert_period")


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer class for Event model object
    """

    class Meta:
        model = Event
        fields = ("id", "type", "text", "timestamp")


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer class for Report model object
    """

    class Meta:
        model = Report
        fields = ("id", "proof", "text", "goal")

