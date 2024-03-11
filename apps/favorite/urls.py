from django.urls import path, include
from favorite.views import favorite_views
urlpatterns = [
    path('', favorite_views)
]