# Generated by Django 4.2.1 on 2023-05-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='vehicle_image',
            field=models.ImageField(upload_to='images/vehicle_images/'),
        ),
    ]
