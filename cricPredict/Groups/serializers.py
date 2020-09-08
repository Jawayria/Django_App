from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'privacy', 'users')

    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.privacy = validated_data.get('privacy', instance.privacy)

        if 'users' in validated_data:
            for user in validated_data['users']:
                instance.users.add(user)

        instance.save()
        return instance
