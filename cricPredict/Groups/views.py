from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import GroupCreationForm
from django.views.generic import CreateView, ListView
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
        return redirect('/group/listgroup')

    def form_invalid(self, form):
        return render(self.request, 'create_group.html', {'form': form})


class ListGroups(ListView):
    model = Group
    template_name = 'groups_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(privacy='public')
