import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client as ClientApi
from .tokens import account_activation_token
from .models import Client as ClientApp, Driver
from .serlializers import *


# Create your views here.
@api_view(['POST'])
def send_code(request):
    phone = request.data.get('phone')
    account_sid = ''
    auth_token = ''
    client = ClientApi(account_sid, auth_token)
    from_number = ''
    if phone:
        auth_code = str(random.randint(100000, 999999))
        message_body = f"Your authentication code is: {auth_code}"
        status_message=''
        try:
            message = client.messages.create(
                body=message_body,
                from_=from_number,
                to='+201012139683'
            )
            status_message=message.status
        except Exception as e:
            print('An error occurred:', e)
            status_message='error'
        user = {
            "phone": phone,
            "code": auth_code
        }
        return Response(status=status.HTTP_200_OK, data={
            "code":auth_code,
            "status_message": status_message,
            "token": account_activation_token.make_token(user)
        })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def check_code(request):
    phone = request.data.get('phone')
    code = request.data.get('code')
    token = request.data.get('token')
    if phone and code and token:
        if account_activation_token.check_token({
            "phone": phone,
            "code": code,
        }, token=token):
            return Response(status=status.HTTP_200_OK, data={
                'auth': True
            })
        else:
            return Response(status=status.HTTP_200_OK, data={
                'auth': False
            })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def get_data_user(request):
    phone = request.data.get('phone')
    if phone:
        user = ClientApp.objects.filter(phone=phone).first()
        if user:
            return Response(status=status.HTTP_200_OK, data={
                'type': 'Client',
                'obj': ClientSerializer(user).data
            })
        else:
            user = Driver.objects.filter(phone=phone).first();
            if user:
                return Response(status=status.HTTP_200_OK, data={
                    'type': 'Driver',
                    'obj': DriverSerializer(user).data
                })
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save_date_client(request):
    client_serilizer = ClientSerializer(data=request.data)
    if client_serilizer.is_valid():
        client_serilizer.save()
        return Response(status=status.HTTP_200_OK, data=client_serilizer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_date_driver(request):
    driver_serilizer = DriverSerializer(data=request.data)
    if driver_serilizer.is_valid():
        driver_serilizer.save()
        return Response(status=status.HTTP_200_OK, data=driver_serilizer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
