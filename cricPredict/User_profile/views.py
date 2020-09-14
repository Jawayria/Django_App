from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from rest_framework.views import APIView

from rest_framework import generics, status

from User_profile.serializers import UserSerializer


class UserAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
   # authentication_classes = (TokenAuthentication,)

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


"""""
class Authentication(GenericAPIView):
    permissions = (IsAuthenticated, )
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializerform = self.get_serializer(data=self.request.data)
        if not serializerform.is_valid():
            raise ParseError(detail=serializerform.errors)
        else:
            username = self.request.POST['username']
            password = self.request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(self.request, user)
                return Response(serializerform.data)
            else:
                return HttpResponse("Invalid Username or Password")
    
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('/')
"""""


class Login(FormView):
    model = User
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = "/group/"

    def form_valid(self, form):
        form = AuthenticationForm(self.request.POST)
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/group/')
        else:
            return HttpResponse("Invalid Username or Password")

    def form_invalid(self, form):
        print(form.errors.as_json())
        return render(self.request, 'login.html', {'form': form})


class Logout(RedirectView):
    def get(self, request1, *args, **kwargs):
        logout(request1)
        return redirect("/")
