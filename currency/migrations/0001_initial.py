# Generated by Django 3.2.20 on 2023-10-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('symbol', models.CharField(max_length=255)),
                ('current_price', models.FloatField()),
                ('market_cap', models.FloatField()),
                ('total_volume', models.FloatField()),
            ],
            options={
                'ordering': ['market_cap'],
            },
        ),
    ]