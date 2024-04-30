"""
Serializers modules
"""

from rest_framework import serializers
#from django.db.models import fields
from .models import User, Group, Goal, Duty, Event, Report


class UserLoginSerializer(serializers.ModelSerializer):
    """
    Serializer class for login info
    """

    class Meta:
        model = User
        fields = ("login", "password")

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class for User model object
    """
    
    class Meta:
        model = User
        fields = ("name", "second_name")


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer class for Group model object
    """

    class Meta:
        model = Group
        fields = ("tag", "is_public", "name", "image")


class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer class for Goal model object
    """

    class Meta:
        model = Goal
        fields = ("name", "is_active", "deadline", "alert_period")


class DutySerializer(serializers.ModelSerializer):
    """
    Serializer class for Duty model object
    """

    class Meta:
        model = Duty
        fields = ("final_value", "current_value", "deadline", "alert_period")


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer class for Event model object
    """

    class Meta:
        model = Event
        field = ("type", "text", "timestamp")


class ReportSerializer(serializers.ModelSerializer):
    """
    Serializer class for Report model object
    """

    class Meta:
        model = Report
        field = ("proof", "text")
