from rest_framework import serializers
from .models import Group


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'privacy', 'admin')
