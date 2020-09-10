from django.db import models
from Groups.models import Group
from User_profile.models import User


# Create your models here.
class League(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    groups = models.ManyToManyField(Group)


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    winner = models.CharField(max_length=50, null=True)
    time = models.DateTimeField()


class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=50)
    score = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField()

    class Meta:
        unique_together = ['user_id', 'group_id', 'match_id']

