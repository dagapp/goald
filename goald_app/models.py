from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class User(models.Model):
    login    = models.CharField  (null=False, max_length=50)
    password = models.BinaryField(null=False)

    name        = models.CharField(null=True, max_length=50)
    second_name = models.CharField(null=True, max_length=50)


class Group(models.Model):
    tag       = models.CharField   (null=False, max_length=50)
    is_public = models.BooleanField(null=False)

    name     = models.CharField  (null=True, max_length=50)
    password = models.BinaryField(null=True)
    image    = models.ImageField (verbose_name='Аватар', upload_to='static/images/groupProfiles', default='\static\images\wNHQWT4wufY.jpg', blank=True, validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))])

    users = models.ManyToManyField('User', related_name='groups')

    leader_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)

    supergroup_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class Goal(models.Model):
    name      = models.CharField   (null=False, max_length=50)
    is_active = models.BooleanField(null=False, default=True)

    deadline     = models.DateTimeField(null=True)
    alert_period = models.TimeField    (null=True)

    group_id  = models.ForeignKey('Group' , null=False, on_delete=models.CASCADE)
    report_id = models.ForeignKey('Report', null=True , on_delete=models.CASCADE)

    supergoal_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE)


class Duty(models.Model):
    final_value   = models.IntegerField(null=False)
    current_value = models.IntegerField(null=False)

    deadline     = models.DateTimeField(null=True)
    alert_period = models.TimeField    (null=True)

    user_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
    goal_id = models.ForeignKey('Goal', null=False, on_delete=models.CASCADE)


class Event(models.Model):
    type      = models.IntegerField (null=False)
    text      = models.CharField    (null=False, max_length=500)
    timestamp = models.DateTimeField(null=False)

    group_id = models.ForeignKey('Group', null=False, on_delete=models.CASCADE)
    goal_id  = models.ForeignKey('Goal' , null=False, on_delete=models.CASCADE)


class Report(models.Model):
    proof = models.ImageField(null=False)

    text = models.CharField(null=True, max_length=500)

    goal_id = models.ForeignKey('Goal', null=False, on_delete=models.CASCADE)

'''
class Message(models.Model):
    text      = models.CharField    (null=False, max_length=500)
    timestamp = models.DateTimeField(null=False) 

    sender_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)


class PrivateChat(models.Model):
    messages = models.ManyToManyField('Message')

    user1_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)
    user2_id = models.ForeignKey('User', null=False, on_delete=models.CASCADE)


class GroupChat(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    group_id = models.OneToOneField('Group', null=False, on_delete=models.CASCADE)
    messages = models.ManyToManyField('Message', null=False, on_delete=models.CASCADE)
'''
