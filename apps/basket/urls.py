from django.contrib import admin
from django.urls import path, include

from basket.views import basket_views, basket_clearing

urlpatterns = [
    path('', basket_views, name='basket'),
    path('basket_clearing/', basket_clearing, name='basket_clearing')
]