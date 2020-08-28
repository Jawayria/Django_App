from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Group(models.Model):
    privacy_choices = [('PB', 'public'), ('PR', 'private')]

    name = models.CharField(max_length=50)
    privacy = models.CharField(max_length=10, choices=privacy_choices, default='PR')
    users = models.ManyToManyField(User, blank=True)
