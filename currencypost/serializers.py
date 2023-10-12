from rest_framework import serializers
from .models import CurrencyPost


class CurrencyPostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    profile_image = serializers.ImageField(
        source='user.userprofile.image', read_only=True
    )
    profile_id = serializers.IntegerField(
        source='user.userprofile.id', read_only=True
    )

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        return obj.user == self.context['request'].user

    class Meta:
        model = CurrencyPost
        fields = [
            'id', 'user', 'topic', 'content', 'created_at', 'updated_at', 'currency', 'image', 'is_owner',
            'profile_image', 'profile_id'
        ]
