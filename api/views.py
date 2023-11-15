from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.serializers import GameSerializers, ArticleSerializers
from games.models import Game
from articles.models import Article


class GameListApiViews(ListAPIView):
    serializer_class = GameSerializers
    queryset = Game.objects.all()


class ArticleListApiViews(ListAPIView):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()