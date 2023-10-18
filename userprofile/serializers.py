from rest_framework import serializers
from .models import UserProfile
from favouritecurrencies.models import FavouriteCurrencies
from favouritecurrencies.serializers import FavouriteCurrenciesSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    favourite_currencies = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        return obj.user == self.context['request'].user

    def get_favourite_currencies(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite_currencies = FavouriteCurrencies.objects.filter(
                user=obj.user
            )
            serializer = FavouriteCurrenciesSerializer(
                favourite_currencies, many=True, context=self.context)
            return serializer.data
        return None

    class Meta:
        model = UserProfile
        fields = [
            'id', 'user', 'name', 'bio', 'image', 'created_at', 'updated_at', 'is_owner', 'favourite_currencies'
        ]
