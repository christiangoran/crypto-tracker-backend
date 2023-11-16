from django.test import TestCase
from currency.models import Currency


class CurrencyModelTest(TestCase):
    def setUp(self):
        Currency.objects.create(
            currency_id='1', name='Bitcoin', symbol='BTC',
            current_price=40000, market_cap=800000000, total_volume=50000
        )

    def test_currency_creation(self):
        bitcoin = Currency.objects.get(name='Bitcoin')
        self.assertEqual(bitcoin.symbol, 'BTC')
        self.assertEqual(bitcoin.current_price, 40000)
