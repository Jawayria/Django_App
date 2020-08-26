from django.db import models

# Create your models here.
from User_profile.models import User


class Group(models.Model):
    privacy_choices = [('PB', 'public'), ['PR', 'private']]

    name = models.CharField(max_length=50)
    privacy = models.CharField(max_length=10, choices=privacy_choices, default='PR')


class UserGroup(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
