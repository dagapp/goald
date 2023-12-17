'''
File for defining modles in Django notation
'''

from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class User(models.Model):
    '''
    Class to represent a User model
    '''

    login = models.CharField(null=False, max_length=50)
    password = models.BinaryField(null=False)

    name = models.CharField(null=True, max_length=50)
    second_name = models.CharField(null=True, max_length=50)


class Group(models.Model):
    '''
    Class to represent a Group model
    '''

    tag = models.CharField(null=False, max_length=50)
    is_public = models.BooleanField(null=False)

    name = models.CharField(null=True, max_length=50)
    password = models.BinaryField(null=True)
    image = models.ImageField(
        null=True,
        upload_to='group',
        default="group/default.jpg",
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=("png", "jpg", "jpeg"))],
    )

    users = models.ManyToManyField("User", related_name="groups")

    leader_id = models.ForeignKey("User", null=False, on_delete=models.CASCADE)

    supergroup_id = models.ForeignKey("self", null=True, on_delete=models.CASCADE)


class Goal(models.Model):
    '''
    class to represent a Goal model
    '''

    name = models.CharField(null=False, max_length=50)
    is_active = models.BooleanField(null=False, default=True)

    deadline = models.DateTimeField(null=True)
    alert_period = models.TimeField(null=True)

    group_id = models.ForeignKey("Group", null=False, on_delete=models.CASCADE)
    report_id = models.ForeignKey("Report", null=True, on_delete=models.CASCADE)

    supergoal_id = models.ForeignKey("self", null=True, on_delete=models.CASCADE)


class Duty(models.Model):
    '''
    class to represent a Duty model
    '''

    final_value = models.IntegerField(null=False)
    current_value = models.IntegerField(null=False)

    deadline = models.DateTimeField(null=True)
    alert_period = models.TimeField(null=True)

    user_id = models.ForeignKey("User", null=False, on_delete=models.CASCADE)
    goal_id = models.ForeignKey("Goal", null=False, on_delete=models.CASCADE)


class Event(models.Model):
    '''
    class to represent a Event model
    '''

    type = models.IntegerField(null=False)
    text = models.CharField(null=False, max_length=500)
    timestamp = models.DateTimeField(null=False)

    group_id = models.ForeignKey("Group", null=False, on_delete=models.CASCADE)
    goal_id = models.ForeignKey("Goal", null=False, on_delete=models.CASCADE)


class Report(models.Model):
    '''
    class to represent a Report model
    '''

    proof = models.ImageField(null=False)

    text = models.CharField(null=True, max_length=500)

    goal_id = models.ForeignKey("Goal", null=False, on_delete=models.CASCADE)
