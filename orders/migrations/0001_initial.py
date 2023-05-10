# Generated by Django 4.2.1 on 2023-05-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChauffeurCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_driver', models.CharField(max_length=255)),
                ('profile_driver', models.CharField(max_length=255)),
                ('name_driver', models.CharField(max_length=255)),
                ('phone_driver', models.CharField(max_length=255)),
                ('car_model', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('numbering_plate', models.CharField(max_length=255)),
                ('vehicle_image', models.CharField(max_length=255)),
                ('latitude_driver', models.FloatField()),
                ('longitude_driver', models.FloatField()),
                ('price', models.FloatField()),
                ('rating', models.FloatField()),
                ('type_car', models.IntegerField()),
                ('minutes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privacy_policy_arabic', models.TextField()),
                ('privacy_policy_english', models.TextField()),
                ('privacy_policy_french', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserCall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_customer', models.CharField(max_length=255)),
                ('profile_customer', models.CharField(max_length=255)),
                ('name_customer', models.CharField(max_length=255)),
                ('phone_customer', models.CharField(max_length=255)),
                ('id_driver', models.CharField(max_length=255)),
                ('profile_driver', models.CharField(max_length=255)),
                ('name_driver', models.CharField(max_length=255)),
                ('phone_driver', models.CharField(max_length=255)),
                ('model_car', models.CharField(max_length=255)),
                ('number_of_passengers', models.IntegerField()),
                ('name_location', models.CharField(max_length=255)),
                ('name_destination', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('numbering_plate', models.CharField(max_length=255)),
                ('vehicle_image', models.CharField(max_length=255)),
                ('latitude_my_location', models.FloatField()),
                ('longitude_my_location', models.FloatField()),
                ('latitude_destination', models.FloatField()),
                ('longitude_destination', models.FloatField()),
                ('latitude_driver', models.FloatField()),
                ('longitude_driver', models.FloatField()),
                ('price', models.FloatField()),
                ('rating_driver', models.FloatField()),
                ('type_car', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('image_payment', models.ImageField(null=True, upload_to='images/images_bay/')),
                ('offers', models.ManyToManyField(to='orders.offer')),
            ],
        ),
    ]