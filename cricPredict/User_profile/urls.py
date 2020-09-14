from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from .views import UserAPIView, Login, Logout, Signup
from . import views

urlpatterns = [
    url(r'^user/$', UserAPIView.as_view(), name="User"),
    url(r'^signup/$', Signup.as_view(), name='Signup'),
    url(r'^user/(?P<pk>[\d]+)/$', UserAPIView.as_view(), name="User APi"),
    url(r'^$', Login.as_view(), name="Login"),
    url(r'^logout/$', Logout.as_view(), name="Logout")
    ]
