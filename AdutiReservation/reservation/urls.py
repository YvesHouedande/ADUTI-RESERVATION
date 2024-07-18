# urls.py

from django.urls import path
from .views import reserver_place, reservation_success

urlpatterns = [
    path('', reserver_place, name='reserver_place'),
    path('success/', reservation_success, name='reservation_success'),
]
