from django.contrib import admin
from django.urls import path, include
from account.views import index_views
from api.views import (GameModelViewSet, ArticleModelViewSet, AccountModelViewSet, GenreModelViewSet,
                       LikeGameModelViewSet, PublisherModelViewSet, LikeArticleModelViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('games', GameModelViewSet)
router.register('articles', ArticleModelViewSet)
router.register('accounts', AccountModelViewSet)
router.register('genres', GenreModelViewSet)
router.register('publishers', PublisherModelViewSet)
router.register('like-article', LikeArticleModelViewSet)
router.register('like-games', LikeGameModelViewSet)

urlpatterns = [
    path('', include(router.urls))


    ]

