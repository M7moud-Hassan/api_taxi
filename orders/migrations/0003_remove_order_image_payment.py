# Generated by Django 4.2.1 on 2023-05-10 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_offers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='image_payment',
        ),
    ]
