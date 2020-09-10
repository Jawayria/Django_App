from rest_framework import serializers
from .models import Group
from User_profile.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'privacy', 'users')

    def create(self, validated_data):
        user = User.objects.filter(username=self.context['request'].user)
        group = Group.objects.create(name=validated_data['name'], privacy=validated_data['privacy'],
                                     admin=self.context['request'].user)
        group.users.add(self.context['request'].user)
        return group

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.privacy = validated_data.get('privacy', instance.privacy)
        if 'users' in validated_data:
            instance.users.clear()
            for user in validated_data['users']:
                instance.users.add(user)

        instance.save()
        return instance
