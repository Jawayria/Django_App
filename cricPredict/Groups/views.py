from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.exceptions import ParseError
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import GroupSerializer
from .forms import GroupCreationForm
from django.views.generic import CreateView, ListView
from .models import Group
from rest_framework.generics import GenericAPIView, CreateAPIView, ListCreateAPIView


# Create your views here.
class GroupAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    permissions = (IsAuthenticated,)
    serializer_class = GroupSerializer

    def post(self, request, *args, **kwargs):
        serializerform = self.get_serializer(data=self.request.data)
        if not serializerform.is_valid():
            raise ParseError(detail="No valid values")
        else:
            serializerform.save(admin=self.request.user)
            form = serializerform.save()
        return Response(serializerform.data)


"""""
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
"""""


class ListGroups(ListView):
    model = Group
    template_name = 'groups_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(privacy='public')

