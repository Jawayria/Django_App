from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView
from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import generics

from User_profile.serializers import UserSerializer


class UserAPIView(APIView):
    permissions = (IsAuthenticated,)
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=self.request.data)
        if not serializer.is_valid():
            raise ParseError(detail="No valid values")
        else:
            form = serializer.save()

        return Response(serializer.data)


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
    success_url = "/group/creategroup"

    def form_valid(self, form):
        form = AuthenticationForm(self.request.POST)
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/group/creategroup')
        else:
            return HttpResponse("Invalid Username or Password")

    def form_invalid(self, form):
        return render(self.request, 'login.html', {'form': form})


class Logout(RedirectView):
    def get(self, request1, *args, **kwargs):
        logout(request1)
        return redirect("/")
