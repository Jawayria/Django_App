from rest_framework import serializers
from rest_framework.fields import CharField

from .models import Group
from User_profile.models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','name', 'privacy', 'users')

    def create(self, validated_data):
        user = User.objects.filter(username=self.context['user'])
        group = Group.objects.create(name=validated_data['name'], privacy=validated_data['privacy'],
                                     admin=self.context['user'])
        group.users.add(self.context['user'])
        return group

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.privacy = validated_data.get('privacy', instance.privacy)
        instance.id = validated_data.get('id', instance.id)
        print(instance.id)

        if 'users' in validated_data:
            instance.users.clear()
            for user in validated_data['users']:
                instance.users.add(user)

        instance.save()
        return instance


class ExtendedGroupSerializer (GroupSerializer):
    class Meta:
        model = Group
        fields = GroupSerializer.Meta.fields + ('admin',)