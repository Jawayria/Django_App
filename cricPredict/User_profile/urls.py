from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^signup/$', views.signup, name="Signup"),
    url(r'^$', views.login_request, name="Login"),
    url(r'^logout/$', views.logout_request, name="Logout")
    ]
