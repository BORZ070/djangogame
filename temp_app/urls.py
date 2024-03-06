from django.contrib import admin
from django.urls import path, include
from temp_app.views import temp_views

urlpatterns = [
    path('', temp_views)
]