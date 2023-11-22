from django.shortcuts import render

from account.models import Profile
from api.serializers import GameSerializers, ArticleSerializers, AccountSerializers, GenreSerializers, PublisherSerializers, LikeArticleSerializers, LikeGameSerializers
from games.models import Game, Genre, Publisher, Like as LikeGame
from articles.models import Article, Like
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


#game
class GameModelViewSet(ModelViewSet):
    serializer_class = GameSerializers
    queryset = Game.objects.all()
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class GenreModelViewSet(ModelViewSet):
    serializer_class = GenreSerializers
    queryset = Genre.objects.all()
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class PublisherModelViewSet(ModelViewSet):
    serializer_class = PublisherSerializers
    queryset = Publisher.objects.all()
    # permission_classes = [IsAuthenticated]
    http_method_names = ['get']


class LikeGameModelViewSet(ModelViewSet):
    serializer_class = LikeGameSerializers
    queryset = LikeGame.objects.all()
    # permission_classes = [IsAuthenticated]


#article
class ArticleModelViewSet(ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    # permission_classes = [IsAuthenticated]


class LikeArticleModelViewSet(ModelViewSet):
    serializer_class = LikeArticleSerializers
    queryset = Like.objects.all()
    # permission_classes = [IsAuthenticated]


#account
class AccountModelViewSet(ModelViewSet):
    serializer_class = AccountSerializers
    queryset = Profile.objects.all()
    # permission_classes = [IsAuthenticated]


