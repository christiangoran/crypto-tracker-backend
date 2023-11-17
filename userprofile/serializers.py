from rest_framework import serializers
from .models import UserProfile
from favouritecurrencies.models import FavouriteCurrencies
from favouritecurrencies.serializers import FavouriteCurrenciesSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    """
    This serializer class handles the conversion of
    UserProfile instances to JSON, and vice versa, to easily
    send/receive data from the client to the server.

    Fields (these are added to the JSON string):
        user: Gets the username of the associated user.
        is_owner: Checks if the request user is the owner of the profile.
        favourite_currencies: Lists the favourite currencies of the user.
        favourite_currencies_count: counts the number of favourite
        currencies the user has.

    Methods:
        get_is_owner: Checks if the request user is the owner of the profile.
        get_favourite_currencies: Lists the favourite currencies if the user
        is authenticated.
        get_favourite_currencies_count: Returns the count of favourite
        currencies for the user.
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_owner = serializers.SerializerMethodField()
    favourite_currencies = serializers.SerializerMethodField()
    favourite_currencies_count = serializers.SerializerMethodField()

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

    def get_favourite_currencies_count(self, obj):
        return FavouriteCurrencies.objects.filter(user=obj.user).count()

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'name',
            'bio',
            'image',
            'created_at',
            'updated_at',
            'is_owner',
            'favourite_currencies',
            'favourite_currencies_count',
        ]
