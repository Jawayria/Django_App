from django.conf.urls import url
from .views import LeagueAPIView, MatchAPIView, PredictionAPIView, ScoreAPIView

urlpatterns = [
    url(r'^league/$', LeagueAPIView.as_view(), name="League"),
    url(r'^match/$', MatchAPIView.as_view(), name="Match"),
    url(r'^prediction/$', PredictionAPIView.as_view(), name="Prediction"),
    url(r'^score/$', ScoreAPIView.as_view(), name="Score"),
    ]
