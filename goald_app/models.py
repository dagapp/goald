from django.db import models

# Create your models here.

class UserModel(models.Model):
    login    = models.CharField  (null=False, max_length=50 )
    password = models.BinaryField(null=False)

    name        = models.CharField(null=True, max_length=50)
    second_name = models.CharField(null=True, max_length=50)

    #group_id = models.ForeignKey('Group', on_delete=models.CASCADE)

'''

class Group(models.Model):
    name = models.CharField(default="", null=False, max_length=20)
    password = models.CharField(blank=True, null=True, max_length=50)
    is_public = models.BooleanField(null=False, default=True)

    leader_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
    goal_id = models.ForeignKey('Goal', null=False, on_delete=models.CASCADE)
    members = models.ManyToManyField('User', null=False, on_delete=models.CASCADE)
    supergroup_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class Goal(models.Model):
    name = models.CharField(default="", null=False, max_length=50)
    is_active = models.BooleanField(null=False, default=True)
    final_value = models.IntegerField(default=0)
    current_value = models.IntegerField(default=0)
    deadline = models.DateTimeField()
    alert_period = models.TimeField(null=True)

    group_id = models.ForeignKey('Group', null=False, on_delete=models.CASCADE)
    #report_id = models.ForeignKey('Report', null=True, on_delete=models.CASCADE)

    supergoal_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class Duty(models.Model):
	amount = models.IntegerField(null=False)
	deadline = models.DateTimeField()
	alert_period = models.TimeField()

	user_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
	goal_id = models.ForeignKey('Goal', null=False, on_delete=models.CASCADE)
'''
     
class Event(models.Model):
    type = models.IntegerField(null=False)
    text = models.CharField(blank=True, null=False, max_length=500)
    timestamp = models.DateTimeField()

    group_id = models.ForeignKey('Group', null=False, on_delete=models.CASCADE)
    goal_id = models.ForeignKey('Goal', null=False, on_delete=models.CASCADE)

class Report(models.Model):
    text = models.CharField(blank=False, null=False, max_length=500)
    proof = models.BinaryField()

    goal_id = models.ForeignKey('Goal', null=False, on_delete=models.CASCADE)

class Message(models.Model):
    text = models.CharField(blank=True, null=False, max_length=500)
    timestamp = models.DateTimeField() 

    sender_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)

class PrivateChat(models.Model):
    user_id1 = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
    user_id2 = models.ForeignKey('User', null=False, on_delete=models.CASCADE)

    messages = models.ManyToManyField('Message', null=False, on_delete=models.CASCADE)

class GroupChat(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    group_id = models.OneToOneField('Group', null=False, on_delete=models.CASCADE)
    messages = models.ManyToManyField('Message', null=False, on_delete=models.CASCADE)
