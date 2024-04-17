from django.contrib import admin
from django.urls import path, include
from account.views import index_views
from api.views import (GameModelViewSet,GameCreateModelViewSet, ArticleModelViewSet, AccountModelViewSet, GenreModelViewSet,
                       LikeGameModelViewSet, PublisherModelViewSet, LikeArticleModelViewSet, BlogModelViewSet)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('games', GameModelViewSet)
router.register('game-create', GameCreateModelViewSet)
router.register('articles', ArticleModelViewSet)
router.register('accounts', AccountModelViewSet)
router.register('genres', GenreModelViewSet)
router.register('publishers', PublisherModelViewSet)
router.register('like-article', LikeArticleModelViewSet)
router.register('like-games', LikeGameModelViewSet)
router.register('blog', BlogModelViewSet)

urlpatterns = [
    path('', include(router.urls))


    ]

