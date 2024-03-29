from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.code = validated_data.get('code', instance.code)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.save()
        return instance


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.profile = validated_data.get('profile', instance.profile)
        instance.date = validated_data.get('date', instance.date)
        instance.department = validated_data.get('department', instance.department)
        instance.personal_address = validated_data.get('personal_address', instance.personal_address)
        instance.model = validated_data.get('model', instance.model)
        instance.color = validated_data.get('color', instance.color)
        instance.numbering_plate = validated_data.get('numbering_plate', instance.numbering_plate)
        instance.vehicle_image = validated_data.get('vehicle_image', instance.vehicle_image)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.state = validated_data.get('state', instance.state)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_subscribe = validated_data.get('is_subscribe', instance.is_subscribe)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance




