from django.conf.urls import url
from .views import LeagueAPIView, MatchAPIView, PredictionAPIView, ScoreAPIView, LeagueMatchesAPIView, \
    GroupLeaguesAPIView

urlpatterns = [
    url(r'^league/$', LeagueAPIView.as_view(), name="League"),
    url(r'^league/(?P<pk>[\d]+)/$', LeagueAPIView.as_view(), name="League"),
    url(r'^group_leagues/(?P<pk>[\d]+)/$', GroupLeaguesAPIView.as_view(), name="Group Leagues View"),
    url(r'^match/$', MatchAPIView.as_view(), name="Match"),
    url(r'^match/(?P<pk>[\d]+)/$', MatchAPIView.as_view(), name="Match"),
    url(r'^league_matches/(?P<pk>[\d]+)/$', LeagueMatchesAPIView.as_view(), name="League Matches View"),
    url(r'^prediction/$', PredictionAPIView.as_view(), name="Prediction"),
    url(r'^prediction/(?P<pk>[\d]+)/$', PredictionAPIView.as_view(), name="Prediction"),
    url(r'^score/$', ScoreAPIView.as_view(), name="Score"),
    url(r'^score/(?P<pk>[\d]+)/$', ScoreAPIView.as_view(), name="Score"),
    ]
