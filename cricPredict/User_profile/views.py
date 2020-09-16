from django.conf import settings
from django.contrib.auth.hashers import check_password
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from .models import User
from User_profile.serializers import UserSerializer


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class Signup(GenericAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (JWTAuthentication, )
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
    authentication_classes = (JWTAuthentication, )
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


class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = ''

    def get(self, request):
        token = str(self.request.headers.get('Authorization')).split()[1]
        cache.set(token, token, CACHE_TTL)
        #print(cache.get(token))
        return Response(status=status.HTTP_200_OK)

