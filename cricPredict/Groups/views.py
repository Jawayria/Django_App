from django.shortcuts import get_object_or_404
from rest_framework import status
from django.views.generic import ListView
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from User_profile.models import User
from .serializers import GroupSerializer


# Create your views here.
class GroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GroupSerializer
    queryset = ''

    def post(self, request):
        print(request.user)
        serializer = GroupSerializer(data=self.request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
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
