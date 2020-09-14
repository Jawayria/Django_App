from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import UserAPIView, Login, Logout
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    url(r'^user/$', UserAPIView.as_view(), name="User"),
    url(r'^signup/$', obtain_auth_token, name='get token'),
    url(r'^user/(?P<pk>[\d]+)/$', UserAPIView.as_view(), name="League"),
    url(r'^$', Login.as_view(), name="Login"),
    url(r'^logout/$', Logout.as_view(), name="Logout")
    ]
