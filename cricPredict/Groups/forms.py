from django import forms
from Groups.models import Group
from django.contrib.auth.models import User


class GroupCreationForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'privacy', 'admin_id']
