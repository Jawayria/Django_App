from django.conf.urls import url
from .views import GroupAPIView, UserGroupsAPIView, OtherPublicGroupsAPIView, RetrieveGroupsDictAPIView

urlpatterns = [
    url(r'^$', GroupAPIView.as_view(), name="Group View"),
    url(r'^(?P<pk>[\d]+)/$', GroupAPIView.as_view(), name="Group View"),
    url(r'^user_groups/(?P<pk>[\d]+)/$', UserGroupsAPIView.as_view(), name="User Groups View"),
    url(r'^other_groups/(?P<pk>[\d]+)/$', OtherPublicGroupsAPIView.as_view(), name="Other Groups View"),
    url(r'^groups_dict/(?P<pk>[\d]+)/$', RetrieveGroupsDictAPIView.as_view(), name="Groups Dictionary View"),
]
