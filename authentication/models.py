from django.db import models
import uuid
# Create your models here.


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    code = models.CharField(max_length=255,default='123456')
    phone = models.CharField(max_length=255)
    profile = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    date = models.DateField()
    department = models.CharField(max_length=255)
    personal_address = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    numbering_plate = models.CharField(max_length=255)
    vehicle_image = models.ImageField(upload_to='images/vehicle_images/')
    gender = models.IntegerField()
    state = models.IntegerField()
    type = models.IntegerField()
    status = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_subscribe = models.BooleanField(default=False)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name