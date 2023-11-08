from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='user.id')
    profile_image = serializers.ReadOnlyField(source='user.image.url')

    class Meta:
        model = get_user_model()
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image',
        )
