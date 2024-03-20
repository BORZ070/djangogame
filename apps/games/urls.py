from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from games.views import list_views, detail_views, like_game_views, favourite_game_views, basket_game_views

# index/games/...
urlpatterns = [
    path('', list_views, name='games_list'),
    path('<int:pk>/', detail_views, name='games_detail'),
    path('games-like/', like_game_views, name='games_like'),
    path('games-favorite/', favourite_game_views, name='games_favourite'),
    path('games-basket/', basket_game_views, name='games_basket'),



]