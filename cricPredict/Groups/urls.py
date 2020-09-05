from django.conf.urls import url

from .views import GroupAPIView

urlpatterns = [
    url(r'^(?P<pk>[\d]+)/$', GroupAPIView.as_view(), name="Group View"),
    url(r'^$', GroupAPIView.as_view(), name="Group View"),
]
