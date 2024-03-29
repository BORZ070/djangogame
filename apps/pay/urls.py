from django.contrib import admin
from django.urls import path, include

from pay.views import pay_views

urlpatterns = [
    path('', pay_views, name='pay')
]