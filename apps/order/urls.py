from django.contrib import admin
from django.urls import path, include

from order.views import order_views

urlpatterns = [
    path('', order_views, name='order')
]