from django.db import models
from Groups.models import Group
from django.contrib.auth.models import User


# Create your models here.
class League(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    groups = models.ManyToManyField(Group)


class Match(models.Model):
    league_id = models.ForeignKey(League, on_delete=models.CASCADE)
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)
    time = models.DateTimeField()


class Prediction(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    prediction = models.CharField(max_length=50)
    score = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        unique_together = ['user_id', 'group_id', 'match_id']


class Score(models.Model):
    Match_Type_Choices = [
        ('R', 'Regular'),
        ('QF', 'Quarter Final'),
        ('SF', 'Semi Final'),
        ('P', 'PlayOff')
    ]
    Result_Choices = [
        ('W', 'Win'),
        ('L', 'Lose'),
        ('D', 'Draw')
    ]

    match_type = models.CharField(max_length=50, choices=Match_Type_Choices)
    result = models.CharField(max_length=20, choices=Result_Choices)
    score = models.IntegerField()
