from rest_framework import serializers
from .models import Match, League, Prediction, Score


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('name', 'start_date', 'end_date')


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('team1', 'team2', 'winner', 'time', 'league_id')


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('prediction', 'score', 'time', 'user', 'match', 'group')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('match_type', 'result', 'score')
