from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import GroupAPIView, ListGroups


urlpatterns = [
    url(r'^creategroup/$', GroupAPIView.as_view(), name="Create Group"),
    url(r'^listgroup/$',ListGroups.as_view(), name="List Group"),
    ]
