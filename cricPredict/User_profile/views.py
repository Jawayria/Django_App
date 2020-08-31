from django.contrib.auth import login, authenticate, logout
from django.core.checks import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/group/creategroup')
            else:
                return HttpResponse("Couldn't create user.")
        else:
            # form = UserCreationForm()
            return HttpResponse(form.errors.as_json())
    return render(request, 'signup.html', {'form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/group/creategroup')
            else:
                return HttpResponse("Invalid username or password.")
        else:
            return HttpResponse("Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_request(request):
    logout(request)
    return redirect("/")
