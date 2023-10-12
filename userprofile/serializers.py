from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        return obj.user == self.context['request'].user

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'name', 'bio', 'image', 'created_at', 'updated_at', 'is_owner'
        ]
