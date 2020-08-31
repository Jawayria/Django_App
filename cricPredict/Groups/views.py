from django.http import HttpResponse
from django.shortcuts import render
from .forms import GroupCreationForm


# Create your views here.
def create_group(request):
    form = GroupCreationForm()
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.admin_id = request.user
            instance.save()
            return HttpResponse("Group Created")
        else:
            return HttpResponse(form.errors.as_json())

    return render(request, 'create_group.html', {'form': form})
