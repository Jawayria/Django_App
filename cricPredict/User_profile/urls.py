from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import UserAPIView, Login, Logout
from . import views

urlpatterns = [
    url(r'^signup/$', UserAPIView.as_view(), name="Signup"),
    url(r'^$', Login.as_view(), name="Login"),
    url(r'^logout/$', Logout.as_view(), name="Logout")
    ]
