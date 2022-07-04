""" profiles app urls file """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
]
