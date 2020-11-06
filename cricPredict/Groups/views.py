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
        joined_groups_ids = Group.objects.filter(users__in=[pk]).values('id')
        queryset = self.get_queryset()
        public_groups = []
        joined_groups = []

        for group in queryset:
            joined = False
            for joined_group_id in joined_groups_ids:
                if group.id == joined_group_id['id']:
                    joined = True
                    joined_groups.append(group)
            if not joined and group.privacy == 'public':
                public_groups.append(group)

        public_groups_serializer = ExtendedGroupSerializer(public_groups, many=True)
        joined_groups_serializer = ExtendedGroupSerializer(joined_groups, many=True)

        return Response(
            {"public_groups": public_groups_serializer.data, "joined_groups": joined_groups_serializer.data})
