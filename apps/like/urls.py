from django.contrib import admin
from django.urls import path, include

from like.views import like_views

urlpatterns = [
    path('', like_views)
]