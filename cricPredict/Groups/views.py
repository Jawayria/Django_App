from django.shortcuts import get_object_or_404
from rest_framework import status
from django.views.generic import ListView
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from .serializers import GroupSerializer
from rest_framework.generics import RetrieveAPIView


# Create your views here.
class GroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer
    queryset = ''

    def post(self, request):
        serializer = GroupSerializer(data=self.request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(request.data)
        return Response(serializer.data)

    def get(self, request, pk=None):
        if pk is not None:
            queryset = Group.objects.get(pk=pk)
            serializer = GroupSerializer(queryset)
        else:
            queryset = Group.objects.filter(privacy='public')
            serializer = GroupSerializer(queryset, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        serializer = GroupSerializer(instance=group, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        Group.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        serializer = GroupSerializer(instance=group, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UserGroupsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer
    queryset = ''

    def get(self, request, pk):
        queryset = Group.objects.filter(users__in=[pk])
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)


class OtherPublicGroupsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer
    queryset = ''

    def get(self, request, pk):
        queryset = Group.objects.filter(privacy='public').exclude(users__in=[pk])
        serializer = GroupSerializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveGroupsDictAPIView(RetrieveAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.all()

    def get(self, request, pk):

        joined_groups_ids = Group.objects.filter(users__in=[pk]).values('id')
        queryset = self.get_queryset()
        publicGroups = []
        joinedGroups = []

        for group in queryset:
            joined = False
            for joined_group_id in joined_groups_ids:
                if group.id == joined_group_id['id']:
                    joined = True
                    joinedGroups.append(group)
            if not joined and group.privacy == 'public':
                publicGroups.append(group)

        public_groups_serializer = GroupSerializer(publicGroups, many=True)
        joined_groups_serializer = GroupSerializer(joinedGroups, many=True)

        return Response(
            {"public_groups": public_groups_serializer.data, "joined_groups": joined_groups_serializer.data})
