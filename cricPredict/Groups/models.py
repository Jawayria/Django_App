from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Group(models.Model):
    privacy_choices = [('public', 'public'), ('private', 'private')]

    name = models.CharField(max_length=50)
    privacy = models.CharField(max_length=10, choices=privacy_choices, default='PR')
    users = models.ManyToManyField(User, blank=True, related_name='group_members')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_admin', null=False)
