from django.conf.urls import url
from .views import UserAPIView, Login, Logout, Signup

urlpatterns = [
    url(r'^list/$', UserAPIView.as_view(), name="User"),
    url(r'^signup/$', Signup.as_view(), name='Signup'),
    url(r'^retrieve_update_destroy/(?P<pk>[\d]+)/$', UserAPIView.as_view(), name="User APi"),
    url(r'^login/$', Login.as_view(), name="Login"),
    url(r'^logout/$', Logout.as_view(), name="Logout")
    ]
