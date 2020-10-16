from django.conf.urls import url

from .views import GroupAPIView, UserGroupsAPIView, OtherPublicGroupsAPIView

urlpatterns = [
    url(r'^$', GroupAPIView.as_view(), name="Group View"),
    url(r'^(?P<pk>[\d]+)/$', GroupAPIView.as_view(), name="Group View"),
    url(r'^user_groups/(?P<pk>[\d]+)/$', UserGroupsAPIView.as_view(), name="User Groups View"),
    url(r'^other_groups/(?P<pk>[\d]+)/$', OtherPublicGroupsAPIView.as_view(), name="Other Groups View"),
]
