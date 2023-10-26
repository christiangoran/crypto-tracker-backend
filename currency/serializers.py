from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            'id', 'currency_id', 'name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'logo_url', 'description',
        ]
