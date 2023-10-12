from django.db import models
from .api import fetch_data_from_coinmarketcap


class Currency(models.Model):
    currency_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    current_price = models.FloatField()
    market_cap = models.FloatField()
    total_volume = models.FloatField()

    class Meta:
        ordering = ['-market_cap']

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def update_currency_data():
        data = fetch_data_from_coinmarketcap()
        for currency in data['data']:
            Currency.objects.update_or_create(
                currency_id=currency['id'],
                defaults={
                    'name': currency['name'],
                    'symbol': currency['symbol'],
                    'current_price': currency['quote']['USD']['price'],
                    'market_cap': currency['quote']['USD']['market_cap'],
                    'total_volume': currency['quote']['USD']['volume_24h']
                }
            )
