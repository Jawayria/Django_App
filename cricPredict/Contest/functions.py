import datetime

from requests import Response

from Contest.models import League, Match
from Contest.serializers import ExtendedLeagueSerializer, ExtendedMatchSerializer


def get_leagues():
    queryset = League.objects.filter(start_date__gte=datetime.date.today())
    queryset = queryset.order_by('start_date')
    serializer = ExtendedLeagueSerializer(queryset, many=True)
    return serializer.data


def get_matches(league_id):
    serializer = ExtendedMatchSerializer(Match.objects.filter(league=league_id).order_by("time"), many=True)
    return serializer.data
