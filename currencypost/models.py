from django.db import models
from django.contrib.auth.models import User
from currency.models import Currency


class CurrencyPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ltn67t',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s post about {self.topic}"
