from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import CreateGroup


urlpatterns = [
    url(r'^creategroup/$', CreateGroup.as_view(), name="Create Group"),
    ]
