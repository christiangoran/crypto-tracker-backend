from rest_framework import serializers
from .models import CurrencyPost


class CurrencyPostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        return obj.user == self.context['request'].user

    class Meta:
        model = CurrencyPost
        fields = [
            'id', 'user', 'topic', 'content', 'created_at', 'updated_at', 'currency', 'image', 'is_owner'
        ]
