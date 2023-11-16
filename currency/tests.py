from django.test import TestCase
from currency.models import Currency
from unittest.mock import patch
from currency.api import fetch_data_from_coinmarketcap


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


class FetchDataFromCoinMarketCapTest(TestCase):
    @patch('currency.api.requests.get')
    def test_fetch_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'data': 'success'}

        data = fetch_data_from_coinmarketcap()
        self.assertEqual(data, {'data': 'success'})
