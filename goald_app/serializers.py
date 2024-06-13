"""
File for defining serializer classes
"""

import secrets
import datetime

from django.contrib.auth.models import User
from numpy import source
from rest_framework import serializers
#from django.db.models import fields
from .models import Group, Goal, Duty, Event, Report, Image, EventType, EVENT_MESSAGES, GROUP_TOKEN_LENGTH


class AuthSerializer(serializers.ModelSerializer):
    """
    Serializer class for auth
    """

    class Meta:
        model = User
        fields = ("username", "password")


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
    group_image = serializers.ImageField(write_only=True, required=True)
    
    class Meta:
        model = Group
        fields = ("id", "tag", "is_public", "name", "group_image", "leader")

    def create(self, validated_data):
        token = secrets.token_urlsafe(GROUP_TOKEN_LENGTH)
        image_file = validated_data.pop('group_image')
        group = Group.objects.create(**validated_data, token=token)
        
        Image.objects.create(image=image_file, group=group)

        Event.objects.create(
            type=int(EventType.GroupCreated),
            text=EVENT_MESSAGES[EventType.GroupCreated],
            timestamp=datetime.datetime.now(),
            group=group,
            goal=None
        )

        return group


class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer class for Goal model object
    """

    #TODO: make that is_active is inavailable on create
    #is_active = serializers.HiddenField(default=True)

    final_value = serializers.IntegerField()
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
        
        final_value = validated_data.pop("final_value")
        goal = Goal.objects.create(**validated_data)

        Duty.objects.create(
            final_value=final_value,
            current_value=0,
            deadline=validated_data.get("deadline"),
            alert_period=validated_data.get("alert_period"),
            user=group.leader,
            goal=goal
        )

        Event.objects.create(
            type=int(EventType.GoalCreated),
            text=EVENT_MESSAGES[EventType.GoalCreated],
            timestamp=datetime.datetime.now(),
            group=group,
            goal=goal
        )

        return goal


class DutySerializer(serializers.ModelSerializer):
    """
    Serializer class for Duty model object
    """

    class Meta:
        model = Duty
        fields = ("id", "goal", "final_value", "current_value", "deadline", "alert_period")


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer class for Event model object
    """

    class Meta:
        model = Event
        fields = ("id", "type", "text", "timestamp", "group", "goal")


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer class for Report model object
    """

    proof = serializers.ImageField(write_only=True, required=True)

    class Meta:
        model = Report
        fields = ("id", "proof", "text", "goal")

    def create(self, validated_data):
        goal = Goal.objects.get(name=validated_data.get("goal"))
        group = goal.group

        report = Report.objects.create(goal=goal, text=validated_data.get("text"))

        image_file = validated_data.pop('proof')
        Image.objects.create(image=image_file, report=report)

        Event.objects.create(
            type=int(EventType.ReportPosted),
            text=EVENT_MESSAGES[EventType.ReportPosted],
            timestamp=datetime.datetime.now(),
            group=group,
            goal=goal
        )

        return report


class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer class for Image model objects
    """

    class Meta:
        model = Image
        fields = ("id", "image", "group", "report")
