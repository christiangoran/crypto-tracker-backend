# Generated by Django 3.2.20 on 2023-11-07 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencypost', '0003_alter_currencypost_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencypost',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]