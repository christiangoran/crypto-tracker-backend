from django.db import models
from .api import fetch_data_from_coinmarketcap, get_cryptocurrency_info


class Currency(models.Model):
    currency_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    current_price = models.FloatField()
    market_cap = models.FloatField()
    total_volume = models.FloatField()
    logo_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-market_cap']

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    def update_currency_data():
        data = fetch_data_from_coinmarketcap()
        for currency in data['data']:
            info = get_cryptocurrency_info(currency['id'])
            Currency.objects.update_or_create(
                currency_id=currency['id'],
                defaults={
                    'description': info['description'],
                    'logo_url': info['logo_url'],
                    'name': currency['name'],
                    'symbol': currency['symbol'],
                    'current_price': currency['quote']['USD']['price'],
                    'market_cap': currency['quote']['USD']['market_cap'],
                    'total_volume': currency['quote']['USD']['volume_24h']
                }
            )
