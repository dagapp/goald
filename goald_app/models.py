from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(default="", null=False, max_length=50)
    second_name = models.CharField(default="", max_length=50)
    password = models.CharField(blank=False, null=False, max_length=50)

    group_id = models.ForeignKey('Group', on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField(default="", null=False, max_length=20)
    password = models.CharField(blank=True, null=True, max_length=50)

    leader_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
    goal_id = models.ForeignKey('Goal', null=False, on_delete=models.CASCADE)


class Goal(models.Model):
    name = models.CharField(default="", null=False, max_length=50)
    goal = models.IntegerField(default=0)
    current_value = models.IntegerField(default=0)
    deadline = models.DateTimeField()

    group_id = models.ForeignKey('Group', null=False, on_delete=models.CASCADE)
