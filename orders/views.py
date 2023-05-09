from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serlializers import *


# Create your views here.

@api_view(['POST'])
def save_date_driver(request):
    order_serializer = OrderSerializer(data=request.data)
    if order_serializer.is_valid():
        order_serializer.save()
        return Response(status=status.HTTP_200_OK, data=order_serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_order_by_type_vehicle(request):
    type = request.data.get('type_car')
    if type:
        orders = Order.objects.filter(type_car=type)
        if orders:
            return Response(data=OrderSerializer(orders, many=True))
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    if orders:
        return Response(data=OrderSerializer(orders, many=True))
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])