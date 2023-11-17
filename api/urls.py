from django.contrib import admin
from django.urls import path, include
from account.views import index_views
from api.views import GameModelViewSet, ArticleModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('games', GameModelViewSet)
router.register('articles', ArticleModelViewSet)

urlpatterns = [
    path('', include(router.urls))


    ]

