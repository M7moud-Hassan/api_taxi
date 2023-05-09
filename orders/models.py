from django.db import models


# Create your models here.
#

class Offer(models.Model):
    id = models.AutoField
    id_driver = models.CharField(max_length=255)
    profile_driver = models.CharField(max_length=255)
    name_driver = models.CharField(max_length=255)
    phone_driver = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    status = models.IntegerField()
    numbering_plate = models.CharField(max_length=255)
    vehicle_image = models.CharField(max_length=255)
    latitude_driver = models.FloatField()
    longitude_driver = models.FloatField()
    price = models.FloatField()
    rating = models.FloatField()
    type_car = models.IntegerField()
    minutes = models.IntegerField()


class Order(models.Model):
    id = models.AutoField
    id_customer = models.CharField(max_length=255)
    profile_customer = models.CharField(max_length=255)
    name_customer = models.CharField(max_length=255)
    phone_customer = models.CharField(max_length=255)
    id_driver = models.CharField(max_length=255)
    profile_driver = models.CharField(max_length=255)
    name_driver = models.CharField(max_length=255)
    phone_driver = models.CharField(max_length=255)
    model_car = models.CharField(max_length=255)
    number_of_passengers = models.IntegerField()
    name_location = models.CharField(max_length=255)
    name_destination = models.CharField(max_length=255)
    status = models.IntegerField()
    numbering_plate = models.CharField(max_length=255)
    vehicle_image = models.CharField(max_length=255)
    latitude_my_location = models.FloatField()
    longitude_my_location = models.FloatField()
    latitude_destination = models.FloatField()
    longitude_destination = models.FloatField()
    latitude_driver = models.FloatField()
    longitude_driver = models.FloatField()
    price = models.FloatField()
    rating_driver = models.FloatField()
    type_car = models.IntegerField()
    minutes = models.IntegerField()
    offers=models.ManyToManyField(Offer)
    image_payment=models.ImageField(upload_to='images/images_bay/',null=True,)


#
#

#
#
class PrivacyPolicy(models.Model):
    privacy_policy_arabic = models.TextField()
    privacy_policy_english = models.TextField()
    privacy_policy_french = models.TextField()
#
#
class UserCall(models.Model):
    id = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    number = models.IntegerField()
    is_active = models.BooleanField()
#
#
class ChauffeurCall(models.Model):
    id = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    number = models.IntegerField()
    is_active = models.BooleanField()
