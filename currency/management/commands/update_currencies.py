from django.core.management.base import BaseCommand
from currency.models import Currency


class Command(BaseCommand):
    """
    To update currencies data from CoinMarketCap, run:
    python3 manage.py update_currencies

    """
    help = 'Update currencies data from CoinMarketCap'

    def handle(self, *args, **kwargs):
        Currency.update_currency_data()
        self.stdout.write(self.style.SUCCESS(
            'Successfully updated currencies data'))
