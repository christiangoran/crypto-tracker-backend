from django.test import TestCase
from django.contrib.auth.models import User
from currency.models import Currency
from favouritecurrencies.models import FavouriteCurrencies


class FavouriteCurrenciesModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.currency = Currency.objects.create(
            currency_id='1', name='Bitcoin', symbol='BTC', current_price=1000.0, market_cap=2000.0, total_volume=3000.0)
        self.favourite = FavouriteCurrencies.objects.create(
            user=self.user, currency=self.currency)

    def test_favourite_creation(self):
        self.assertEqual(self.favourite.user, self.user)
        self.assertEqual(self.favourite.currency, self.currency)
