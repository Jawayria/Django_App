from django.http import HttpResponse
from django.shortcuts import render
from .forms import GroupCreationForm


# Create your views here.
def create_group(request):
    form = GroupCreationForm()
    if request.method == 'POST':
        form = GroupCreationForm(request.POST)
        form.fields["admin_id"].initial = request.user.id
        if form.is_valid():
            form.cleaned_data["admin_id"] = request.user.id
            form.save()
            return HttpResponse("Group Created")
        else:
            return HttpResponse(form.errors.as_json())

    return render(request, 'create_group.html', {'form': form})
