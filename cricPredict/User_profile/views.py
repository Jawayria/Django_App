from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, RedirectView


# Create your views here.
class Signup(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = "/group/creategroup"

    def form_valid(self, form):
        form = UserCreationForm(self.request.POST)
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('/group/creategroup')
        else:
            return HttpResponse("Couldn't create user.")

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_json())


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
        return HttpResponse(form.errors.as_json())


class Logout(RedirectView):

    def get(self, request1, *args, **kwargs):
        logout(request1)
        return redirect("/")
