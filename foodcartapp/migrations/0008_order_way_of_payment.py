# Generated by Django 3.2.15 on 2023-05-29 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0007_auto_20230529_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='way_of_payment',
            field=models.CharField(choices=[('Наличные', 'Наличные'), ('Картой', 'Картой')], default='Картой', max_length=50, verbose_name='Способ оплаты'),
        ),
    ]
