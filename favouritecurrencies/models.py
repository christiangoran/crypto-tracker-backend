from django.db import models
from django.contrib.auth.models import User
from currency.models import Currency


class FavouriteCurrencies(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    currency = models.ForeignKey(
        Currency, related_name='favourite', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'currency']

    def __str__(self):
        return f"{self.user.username}' favourite currencies"
