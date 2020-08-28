from django.http import HttpResponse
from django.shortcuts import render
from .forms import GroupCreationForm


# Create your views here.
def create_group(request):
    form = GroupCreationForm()
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Invalid Data")

    return render(request, 'create_group.html', {'form': form})
