from django.http import HttpResponse
from django.shortcuts import render
from .forms import GroupCreationForm
from django.views.generic import CreateView
from .models import Group


# Create your views here.
class CreateGroup(CreateView):
    model = Group
    form_class = GroupCreationForm
    template_name = 'create_group.html'

    def form_valid(self, form):
        form = GroupCreationForm(self.request.POST)
        instance = form.save(commit=False)
        instance.admin = self.request.user
        instance.save()
        return HttpResponse("Group Created")

    def form_invalid(self, form):
        return HttpResponse(form.errors.as_json())

