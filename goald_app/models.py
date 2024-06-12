"""
File for defining modles in Django notation
"""

import datetime
import string

from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator


DEFAULT_NAME_CHARS = string.ascii_letters + string.digits
DEFAULT_NAME_SIZE = 10


class Group(models.Model):
    """
    Class to represent a Group model
    """

    tag = models.CharField(null=False, max_length=50)
    is_public = models.BooleanField(null=False, default=True)

    name = models.CharField(null=True, max_length=50)
    password = models.BinaryField(null=True)
    image = models.ImageField(
        null=True,
        upload_to="group",
        default="group/default.jpg",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=("png", "jpg", "jpeg"))],
    )

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="users_groups")

    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE, related_name="groups_leader"
    )

    supergroup = models.ForeignKey(
        "self", null=True, on_delete=models.CASCADE, related_name="groups_supergroup"
    )

    def __str__(self) -> str:
        return self.tag


class Goal(models.Model):
    """
    Class to represent a Goal model
    """

    name = models.CharField(null=False, max_length=50)
    is_active = models.BooleanField(null=False, default=True)

    deadline = models.DateTimeField(null=True)
    alert_period = models.DurationField(null=True)

    reports = models.ManyToManyField("Report", related_name="reports")

    group = models.ForeignKey(
        "Group", null=False, on_delete=models.CASCADE, related_name="goals_group"
    )

    supergoal = models.ForeignKey(
        "self", null=True, on_delete=models.CASCADE, related_name="goals_supergoal"
    )

    def __str__(self) -> str:
        return self.name


class Duty(models.Model):
    """
    Class to represent a Duty model
    """

    final_value = models.IntegerField(null=False, default=0)
    current_value = models.IntegerField(null=False, default=0)

    deadline = models.DateTimeField(null=True)
    alert_period = models.DurationField(null=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE, related_name="duties_user"
    )
    goal = models.ForeignKey(
        "Goal", null=False, on_delete=models.CASCADE, related_name="duties_goal"
    )


class Event(models.Model):
    """
    Class to represent a Event model
    """

    type = models.IntegerField(null=False, default=0)
    text = models.CharField(null=False, max_length=500, default="")
    timestamp = models.DateTimeField(null=False, default=datetime.datetime.now)

    group = models.ForeignKey(
        "Group", null=True, on_delete=models.CASCADE, related_name="events_group"
    )
    goal = models.ForeignKey(
        "Goal", null=True, on_delete=models.CASCADE, related_name="events_goal"
    )


class Report(models.Model):
    """
    Class to represent a Report model
    """

    proof = models.ImageField(null=False)

    text = models.CharField(null=True, max_length=1024)

    goal = models.ForeignKey(
        "Goal", null=False, on_delete=models.CASCADE, related_name="reports_goal"
    )
