from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from .serializers import GroupSerializer, ExtendedGroupSerializer
from rest_framework.generics import RetrieveAPIView


# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):

    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def create(self, request):
        serializer = GroupSerializer(data=self.request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def categorized_groups(self, request, pk=None):
        queryset = self.get_queryset()

        user_groups = queryset.filter(users__in=[pk])
        user_group_ids = user_groups.values('id')
        public_groups = queryset.filter(privacy='public').exclude(id__in=user_group_ids)

        public_groups_serializer = ExtendedGroupSerializer(public_groups, many=True)
        joined_groups_serializer = ExtendedGroupSerializer(user_groups, many=True)

        return Response(
            {"public_groups": public_groups_serializer.data, "joined_groups": joined_groups_serializer.data})
