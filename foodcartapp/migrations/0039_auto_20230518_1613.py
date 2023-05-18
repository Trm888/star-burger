# Generated by Django 3.2.15 on 2023-05-18 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0038_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='foodcartapp.order'),
            preserve_default=False,
        ),
    ]
