from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import GroupAPIView, ListGroups


urlpatterns = [
    url(r'^(?P<pk>[\d]+)/$', GroupAPIView.as_view(), name="Delete Group"),
    url(r'^$', GroupAPIView.as_view(), name="Create Group"),
    ]
