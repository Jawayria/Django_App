from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import UserAPIView, Login, Logout
from . import views

urlpatterns = [
    url(r'^user/$', UserAPIView.as_view(), name="User"),
    url(r'^user/(?P<pk>[\d]+)/$', UserAPIView.as_view(), name="League"),
    url(r'^$', Login.as_view(), name="Login"),
    url(r'^logout/$', Logout.as_view(), name="Logout")
    ]
