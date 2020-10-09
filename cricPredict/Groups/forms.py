from django import forms
from Groups.models import Group
from User_profile.models import User


class GroupCreationForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ['name', 'privacy']
