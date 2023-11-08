from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from games.views import list_views



# index/games/...
urlpatterns = [
    path('', list_views, name='games_list'),



]