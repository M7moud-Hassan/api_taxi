from rest_framework import serializers
from .models import *


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    offers=OfferSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'

