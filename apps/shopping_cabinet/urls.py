from django.contrib import admin
from django.urls import path, include

from shopping_cabinet.views import cabinet_views

urlpatterns = [
    path('', cabinet_views, name='cabinet')
]