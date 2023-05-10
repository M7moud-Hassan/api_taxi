# Generated by Django 4.2.1 on 2023-05-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_id_driver_remove_order_name_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='id_driver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='latitude_destination',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='latitude_driver',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='latitude_my_location',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='longitude_destination',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='longitude_driver',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='longitude_my_location',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='minutes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='model_car',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name_customer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name_destination',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name_driver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name_location',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='number_of_passengers',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='numbering_plate',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone_customer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone_driver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='profile_customer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='profile_driver',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='rating_driver',
            field=models.DecimalField(decimal_places=10, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='type_car',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='vehicle_image',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]