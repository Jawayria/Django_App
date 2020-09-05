from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ParseError
from django.views.generic import ListView
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Group
from .serializers import GroupSerializer


# Create your views here.
class GroupAPIView(APIView):
    permissions = (IsAuthenticated,)
    serializer_class = GroupSerializer
    queryset = ''

    def post(self, request):
        serializer = GroupSerializer(data=self.request.data)
        if not serializer.is_valid():
            raise ParseError(detail="No valid values")
        else:
            serializer.save(admin=self.request.user)
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


"""""
    def delete(self, request, *args, **kwargs):
  #      group = self.get_object()
        self.get_object(request.query_params['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""""

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
