from django.conf.urls import url

from .views import GroupAPIView, UserGroupsAPIView

urlpatterns = [
    url(r'^(?P<pk>[\d]+)/$', GroupAPIView.as_view(), name="Group View"),
    url(r'^user_groups/(?P<pk>[\d]+)/$', UserGroupsAPIView.as_view(), name="User Groups View"),
    url(r'^$', GroupAPIView.as_view(), name="Group View"),
]
