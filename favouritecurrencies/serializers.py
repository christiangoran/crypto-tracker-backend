from rest_framework import serializers
from .models import FavouriteCurrencies
from django.db import IntegrityError


class FavouriteCurrenciesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        return obj.user == self.context['request'].user

    class Meta:
        model = FavouriteCurrencies
        fields = ['id', 'user', 'currency', 'created_at', 'is_owner']

    def validate(self, data):
        user = self.context['request'].user
        currency = data.get('currency')

        if FavouriteCurrencies.objects.filter(
            user=user,
            currency=currency
        ).exists():
            raise serializers.ValidationError(
                "You have already added this currency to your favourites")

        return data
