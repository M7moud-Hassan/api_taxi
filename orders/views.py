
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serlializers import *
from authentication.serlializers import *


# Create your views here.

@api_view(['POST'])
def save_date_order(request):
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
            return Response(data=OrderSerializer(orders, many=True).data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    if orders:
        return Response(data=OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def get_offers_by_orders(request):
    id = request.data.get('id_order')
    if id:
        order = Order.objects.filter(id=id).first()
        if order:
            offers = order.offers.all()
            if offers:
                return Response(OfferSerializer(offers, many=True).data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def upload_image_bay(request):
    order_id = request.data.get('order_id')
    image = request.data.get('image')
    if order_id:
        order = Order.objects.filter(id=order_id).first()
        if order:
            order.image_payment = image
            order.save()
            return Response(data={
                "image_urls":'/media/images/images_bay/' + order.image_payment.url
            })
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_canceled(request):
    orders = Order.objects.filter(status=Status.cancel)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_start_finish(request):
    orders = Order.objects.filter(status=Status.start_finish)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_start_done(request):
    orders = Order.objects.filter(status=Status.done)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_normal(request):
    orders = Order.objects.filter(status=Status.normal)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_client(request):
    clients = Client.objects.all()
    if clients:
        return Response(ClientSerializer(clients, many=True).data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_drivers(request):
    drivers = Driver.objects.all()
    if drivers:
        return Response(DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['put'])
def update_client(request):
    id = request.data.get('id')
    if id:
        client = get_object_or_404(Client, id=id)
        client_serializer = ClientSerializer(client, data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(data=client_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['put'])
def update_driver(request):
    id = request.data.get('id')
    if id:
        driver = get_object_or_404(Driver, id=id)
        driver_serilizer = DriverSerializer(driver,data=request.data)
        if driver_serilizer.is_valid():
            driver_serilizer.save()
            return Response(status=status.HTTP_200_OK, data=driver_serilizer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_old(request):
    drivers = Driver.objects.filter(is_active=True, is_subscribe=True, status=Status.accept)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class Status:
    cancel = 0
    start_finish = 1
    done = 2
    normal = 3
    accept = 4
    under_review = 5
    reject = 6



@api_view(['GET'])
def get_driver_old_not_subscribe(request):
    drivers = Driver.objects.filter(is_active=True, is_subscribe=False, status=Status.accept)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_new(request):
    drivers = Driver.objects.filter(is_active=True, is_subscribe=True, status=Status.under_review)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_banned(request):
    drivers = Driver.objects.filter(is_active=False)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_reject(request):
    drivers = Driver.objects.filter(status=Status.reject)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
