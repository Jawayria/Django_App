from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from rest_framework.views import APIView

from rest_framework import generics, status

from User_profile.serializers import UserSerializer


class Signup(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=self.request.data['username'])
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(res, status.HTTP_201_CREATED)


class Login(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = ''

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=self.request.data['username'])

        if user is not None and check_password(self.request.data['password'], user.password):
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            return Response(res, status.HTTP_201_CREATED)

        else:
            return Response(status.HTTP_400_BAD_REQUEST)


class UserAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = UserSerializer
    queryset = ''

    def get(self, request, pk=None):
        if pk is not None:
            queryset = User.objects.get(pk=pk)
            serializer = UserSerializer(queryset)
        else:
            queryset = User.objects.all()
            serializer = UserSerializer(queryset, many=True)

        return Response(serializer.data)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk):
        User.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class Logout(RedirectView):
    def get(self, request1, *args, **kwargs):
        logout(request1)
        return redirect("/")
