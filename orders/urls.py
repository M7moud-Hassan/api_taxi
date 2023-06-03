"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from  .views import  *
urlpatterns = [
    path('saveDataOrder/', save_date_order),
    path('getOrderByTypeVehicle/',get_order_by_type_vehicle),
    path('getOrders/',get_orders),
    path('getOffersByOrders/',get_offers_by_orders),
    path('uploadImageBay/',upload_image_bay),
    path('getOrdersCanceled/',get_orders_canceled),
    path('getOrdersStartFinish/',get_orders_start_finish),
    path('getOrdersStartDone/',get_orders_start_done),
    path('getOrdersNormal/',get_orders_normal),
    path('getAllClient/',get_all_client),
    path('getAllDrivers/',get_all_drivers),
    path('updateClient/',update_client),
    path('updateDriver/',update_driver),
    path('getDriverOld/',get_driver_old),
    path('getDriverOldNotSubscribe/',get_driver_old_not_subscribe),
    path('getDriverNew/',get_driver_new),
    path('getDriverBanned/',get_driver_banned),
    path('getDriverReject/',get_driver_reject),
    path('getPrivacyPolicy/',get_privacy_policy),
    path('getRide/',get_ride),
    path('updateRide/',update_order),
    path('updateRatingChauffeur/',update_rating_chauffeur),
    path('addOffer/',add_offer),
    path('deleteOffer/',delete_offer)
]
