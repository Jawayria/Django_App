from django.conf.urls import url
from .views import LeagueAPIView, PredictionAPIView, LeagueMatchesAPIView, \
    GroupLeaguesAPIView, MatchPredictionsAPIView, UserPredictionsAPIView, RankingsAPIView, MatchListCreateView, \
    MatchView, GetLeagueAPIView

urlpatterns = [
    url(r'^league/get/$', GetLeagueAPIView.as_view(), name="GetLeague"),
    url(r'^league/get/(?P<pk>[\d]+)/$', GetLeagueAPIView.as_view(), name="GetLeague"),
    url(r'^league/$', LeagueAPIView.as_view(), name="League"),
    url(r'^league/(?P<pk>[\d]+)/$', LeagueAPIView.as_view(), name="League"),
    url(r'^group_leagues/(?P<pk>[\d]+)/$', GroupLeaguesAPIView.as_view(), name="Group Leagues View"),
    url(r'^match/$', MatchListCreateView.as_view(), name="Match"),
    url(r'^match/(?P<pk>[\d]+)/$', MatchView.as_view(), name="Match"),
    url(r'^league_matches/(?P<pk>[\d]+)/$', LeagueMatchesAPIView.as_view(), name="League Matches View"),
    url(r'^prediction/$', PredictionAPIView.as_view(), name="Prediction"),
    url(r'^prediction/(?P<pk>[\d]+)/$', PredictionAPIView.as_view(), name="Prediction"),
    url(r'^match_predictions/(?P<match>[\d]+)/(?P<group>[\d]+)/$', MatchPredictionsAPIView.as_view(),
        name="Match Predictions View"),
    url(r'^user_predictions/(?P<user>[\d]+)/(?P<league>[\d]+)/(?P<group>[\d]+)/$', UserPredictionsAPIView.as_view(),
        name="User Predictions View"),
    url(r'^rankings/(?P<group>[\d]+)/(?P<league>[\d]+)/$', RankingsAPIView.as_view(),
        name="Group League View")
    ]
