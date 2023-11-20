from django.shortcuts import render

from api.serializers import GameSerializers, ArticleSerializers
from games.models import Game
from articles.models import Article
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class GameModelViewSet(ModelViewSet):
    serializer_class = GameSerializers
    queryset = Game.objects.all()
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']

class ArticleModelViewSet(ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated]


