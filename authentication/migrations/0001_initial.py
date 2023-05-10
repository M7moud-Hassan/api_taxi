# Generated by Django 4.2.1 on 2023-05-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('code', models.CharField(default='123456', max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('profile', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=255)),
                ('personal_address', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('numbering_plate', models.CharField(max_length=255)),
                ('vehicle_image', models.CharField(max_length=255)),
                ('gender', models.IntegerField()),
                ('state', models.IntegerField()),
                ('type', models.IntegerField()),
                ('status', models.IntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_subscribe', models.BooleanField(default=False)),
                ('rating', models.FloatField()),
            ],
        ),
    ]
