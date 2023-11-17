from django.test import TestCase
from django.contrib.auth.models import User
from currency.models import Currency
from favouritecurrencies.models import FavouriteCurrencies
from rest_framework.test import APITestCase, APIRequestFactory
from favouritecurrencies.serializers import FavouriteCurrenciesSerializer


class FavouriteCurrenciesModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.currency = Currency.objects.create(
            currency_id='1', name='Bitcoin', symbol='BTC',
            current_price=1000.0, market_cap=2000.0, total_volume=3000.0
        )

    def test_favourite_creation(self):
        favourite = FavouriteCurrencies.objects.create(
            user=self.user, currency=self.currency)
        self.assertEqual(favourite.user, self.user)
        self.assertEqual(favourite.currency, self.currency)

    def test_valid_serializer(self):
        factory = APIRequestFactory()
        request = factory.get('/')  # Test request
        request.user = self.user

        valid_serializer_data = {'currency': self.currency.id}
        context = {'request': request}
        serializer = FavouriteCurrenciesSerializer(
            data=valid_serializer_data, context=context)
        self.assertTrue(serializer.is_valid())

    def test_unique_constraint(self):
        FavouriteCurrencies.objects.create(
            user=self.user, currency=self.currency)

        factory = APIRequestFactory()
        request = factory.get('/')
        request.user = self.user

        serializer_data = {'currency': self.currency.id}
        context = {'request': request}
        serializer = FavouriteCurrenciesSerializer(
            data=serializer_data, context=context)

        self.assertFalse(serializer.is_valid())
        if 'non_field_errors' in serializer.errors:
            error_detail = serializer.errors['non_field_errors'][0]
            self.assertEqual(
                str(error_detail),
                'You have already added this currency to your favourites'
            )
        else:
            self.fail(
                "Unique constraint violation not captured by the serializer")
