import datetime

from Contest.models import League
from Contest.serializers import ExtendedLeagueSerializer


def get_leagues():
    queryset = League.objects.filter(start_date__gte=datetime.date.today())
    queryset = queryset.order_by('start_date')
    serializer = ExtendedLeagueSerializer(queryset, many=True)
    return serializer.data