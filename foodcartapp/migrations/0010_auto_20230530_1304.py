# Generated by Django 3.2.15 on 2023-05-30 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0009_order_restaurateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='order',
            name='lon',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lon',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
    ]
