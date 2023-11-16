from django.test import TestCase
from django.contrib.auth.models import User
from currency.models import Currency
from currencypost.models import CurrencyPost


class CurrencyPostModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='testie', password='password123')
        currency = Currency.objects.create(
            currency_id='1', name='Bitcoin', symbol='BTC', current_price=40000, market_cap=800000000, total_volume=50000)
        CurrencyPost.objects.create(user=user, topic='Bitcoin Rising',
                                    content='Exciting times for Bitcoin!', currency=currency)

    def test_currency_post_creation(self):
        post = CurrencyPost.objects.get(topic='Bitcoin Rising')
        self.assertEqual(post.user.username, 'testie')
        self.assertEqual(post.content, 'Exciting times for Bitcoin!')
        self.assertEqual(post.currency.name, 'Bitcoin')
