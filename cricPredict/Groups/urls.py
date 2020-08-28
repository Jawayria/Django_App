from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^creategroup/$', views.create_group, name="Create Group"),
    ]
