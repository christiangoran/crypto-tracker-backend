# Generated by Django 3.2.20 on 2023-10-26 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_alter_currency_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='logo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
