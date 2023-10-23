from django.db import models

# Create your models here.

class UserModel(models.Model):
    login    = models.CharField  (null=False, max_length=50)
    password = models.BinaryField(null=False)

    name        = models.CharField(null=True, max_length=50)
    second_name = models.CharField(null=True, max_length=50)


class GroupModel(models.Model):
    tag       = models.CharField   (null=False)
    is_public = models.BooleanField(null=False)

    name     = models.CharField  (null=True, max_length=50)
    password = models.BinaryField(null=True)
    image    = models.ImageField (null=True)

    members = models.ManyToManyField('UserModel')

    leader_id = models.ForeignKey('UserModel', null=False, on_delete=models.CASCADE)
    goal_id   = models.ForeignKey('GoalModel', null=False, on_delete=models.CASCADE)

    supergroup_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class GoalModel(models.Model):
    name      = models.CharField   (null=False, max_length=50)
    is_active = models.BooleanField(null=False, default=True)

    deadline = models.DateTimeField(null=True)
    alert_period = models.TimeField(null=True)

    group_id  = models.ForeignKey('GroupModel' , null=False, on_delete=models.CASCADE)
    report_id = models.ForeignKey('ReportModel', null=True , on_delete=models.CASCADE)

    supergoal_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class DutyModel(models.Model):
    final_value   = models.IntegerField(null=False)
    current_value = models.IntegerField(null=False)

    deadline = models.DateTimeField(null=True)
    alert_period = models.TimeField(null=True)

    user_id = models.ForeignKey('UserModel', null=False, on_delete=models.CASCADE)
    goal_id = models.ForeignKey('GoalModel', null=False, on_delete=models.CASCADE)


class EventModel(models.Model):
    type      = models.IntegerField (null=False)
    text      = models.CharField    (null=False, max_length=500)
    timestamp = models.DateTimeField(null=False)

    group_id = models.ForeignKey('GroupModel', null=False, on_delete=models.CASCADE)
    goal_id  = models.ForeignKey('GoalModel' , null=False, on_delete=models.CASCADE)


class ReportModel(models.Model):
    proof = models.ImageField(null=False)

    text = models.CharField (null=True, max_length=500)

    goal_id = models.ForeignKey('GoalModel', null=False, on_delete=models.CASCADE)

'''
class MessageModel(models.Model):
    text      = models.CharField    (null=False, max_length=500)
    timestamp = models.DateTimeField(null=False) 

    sender_id = models.ForeignKey('UserModel', null=False, on_delete=models.CASCADE)


class PrivateChatModel(models.Model):
    messages = models.ManyToManyField('MessageModel')

    user1_id = models.ForeignKey('UserModel', null=False, on_delete=models.CASCADE)
    user2_id = models.ForeignKey('UserModel', null=False, on_delete=models.CASCADE)


class GroupChatModel(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    group_id = models.OneToOneField('GroupModel', null=False, on_delete=models.CASCADE)
    messages = models.ManyToManyField('MessageModel', null=False, on_delete=models.CASCADE)
'''