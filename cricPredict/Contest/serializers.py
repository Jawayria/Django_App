from rest_framework import serializers
from .models import Match, League, Prediction


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ('id', 'name', 'start_date', 'end_date')


class ExtendedLeagueSerializer(LeagueSerializer):
    class Meta:
        model = League
        fields = LeagueSerializer.Meta.fields + ('groups',)


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('id','team1', 'team2', 'time', 'league')


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


class RankingsSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    score__sum = serializers.IntegerField()
