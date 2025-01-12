# Generated by Django 3.2.15 on 2023-05-29 03:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0006_order_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='called_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата звонка'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата доставки'),
        ),
        migrations.AddField(
            model_name='order',
            name='registered_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата регистрации заказа'),
        ),
    ]
