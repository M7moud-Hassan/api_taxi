from django.db import models
import uuid

# Create your models here.
#

class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_driver = models.CharField(max_length=255)
    profileDriver = models.CharField(max_length=255)
    nameDriver = models.CharField(max_length=255)
    phoneDriver = models.CharField(max_length=255)
    carModel = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    numberingPlate = models.CharField(max_length=255)
    vehicleImage = models.CharField(max_length=255)
    longitudeDriver = models.DecimalField(max_digits=20,decimal_places=10)
    latitudeDriver =  models.DecimalField(max_digits=20,decimal_places=10)
    price =  models.DecimalField(max_digits=20,decimal_places=10)
    rating =  models.DecimalField(max_digits=20,decimal_places=10)
    typeCar = models.IntegerField()
    minutes = models.IntegerField()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idCustomer = models.CharField(max_length=255)
    profileCustomer = models.CharField(max_length=255)
    nameCustomer = models.CharField(max_length=255)
    phoneCustomer = models.CharField(max_length=255)
    idDriver = models.CharField(max_length=255)
    profileDriver = models.CharField(max_length=255)
    nameDriver = models.CharField(max_length=255)
    phoneDriver = models.CharField(max_length=255)
    modelCar = models.CharField(max_length=255)
    numberOfPassengers = models.CharField(max_length=255)
    nameLocation = models.CharField(max_length=255)
    nameDestinations = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    numberingPlate = models.CharField(max_length=255)
    vehicleImage = models.CharField(max_length=255)
    latitudeMyLocation = models.DecimalField(max_digits=20,decimal_places=10)
    longitudeMyLocation = models.DecimalField(max_digits=20,decimal_places=10)
    latitudeDestination = models.DecimalField(max_digits=20,decimal_places=10)
    longitudeDestination = models.DecimalField(max_digits=20,decimal_places=10)
    latitudeDriver = models.DecimalField(max_digits=20,decimal_places=10)
    longitudeDriver = models.DecimalField(max_digits=20,decimal_places=10)
    price = models.DecimalField(max_digits=20,decimal_places=10)
    ratingDriver = models.DecimalField(max_digits=20,decimal_places=10)
    typeCar = models.IntegerField()
    minutes = models.IntegerField()
    offers=models.ManyToManyField(Offer,blank=True)
    imagePayment=models.CharField(max_length=255)

#
#
class PrivacyPolicy(models.Model):
    privacyPolicyArabic = models.TextField()
    privacyPolicyEnglish = models.TextField()
    privacyPolicyFrench = models.TextField()
#
#
class UserCall(models.Model):
    id =models.AutoField
    content = models.CharField(max_length=255)
    number = models.IntegerField()
    active = models.BooleanField()
#
#
class ChauffeurCall(models.Model):
    id =models.AutoField
    content = models.CharField(max_length=255)
    number = models.IntegerField()
    active = models.BooleanField()
