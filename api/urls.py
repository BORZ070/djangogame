from django.contrib import admin
from django.urls import path, include
from account.views import index_views
from api.views import GameListApiViews, ArticleListApiViews

urlpatterns = [
    path('gamelist/', GameListApiViews.as_view(), name='gamelist'),
    path('articlelist/', ArticleListApiViews.as_view(), name='articlelist')


    ]

