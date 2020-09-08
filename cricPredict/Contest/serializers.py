from rest_framework import serializers
from .models import Match, League, Prediction, Score


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('name', 'start_date', 'end_date')


class ExtendedLeagueSerializer(LeagueSerializer):
    class Meta:
        model = League
        fields = LeagueSerializer.Meta.fields + ('groups',)


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('team1', 'team2', 'time', 'league_id')


class ExtendedMatchSerializer(MatchSerializer):
    class Meta:
        model = Match
        fields = MatchSerializer.Meta.fields + ('winner',)


class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = ('prediction', 'time', 'user', 'match', 'group')


class ExtendedPredictionSerializer(PredictionSerializer):
    class Meta:
        model = Prediction
        fields = PredictionSerializer.Meta.fields + ('score',)


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('match_type', 'result', 'score')
