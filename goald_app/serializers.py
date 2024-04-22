from rest_framework import serializers
from django.db.models import fields
from .models import User, Group, Goal, Duty, Event, Report


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User model object
    """

    """
    name = serializers.CharField(max_length=50)
    second_name = serializers.CharField(max_length=50)
    """
    
    class Meta:
        model = User
        fields = ("name", "second_name")


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer class for Group model object
    """

    """
    tag = serializers.CharField(max_length=50)
    is_public = serializers.BooleanField()

    name = serializers.CharField(max_length=50)
    image = serializers.CharField()

    users = serializers.ListField()
    """

    class Meta:
        model = Group
        fields = ("tag", "is_public", "name", "image")


class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer class for Goal model object
    """

    """
    name = serializers.CharField(max_length=50)
    is_active = serializers.BooleanField()

    deadline = serializers.DateTimeField()
    alert_period = serializers.DurationField()
    """

    class Meta:
        model = Goal
        fields = ("name", "is_active", "deadline", "alert_period")


class DutySerializer(serializers.ModelSerializer):
    """
    Serializer class for Duty model object
    """

    """
    final_value = serializers.IntegerField()
    current_value = serializers.IntegerField()

    deadline = serializers.DateTimeField()
    alert_period = serializers.DurationField()
    """

    class Meta:
        model = Duty
        fields = ("final_value", "current_value", "deadline", "alert_period")


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer class for Event model object
    """

    """
    type = serializers.IntegerField()
    text = serializers.CharField()
    timestamp = serializers.DateTimeField()
    """

    class Meta:
        model = Event
        field = ("type", "text", "timestamp")


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer class for Report model object
    """

    """
    proof = serializers.CharField()

    text = serializers.CharField(max_length=1024)
    """

    class Meta:
        model = Report
        field = ("proof", "text")
