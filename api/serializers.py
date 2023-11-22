from rest_framework import serializers

from account.models import Profile
from games.models import Game, Genre,Publisher, Like as LikeGame
from articles.models import Article, Like


#Game
class GenreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'genre']


class PublisherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'publisher']


class GameSerializers(serializers.ModelSerializer):

    genre = GenreSerializers()
    publisher = PublisherSerializers()
    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Game
        fields = [
            'id',
            'name',
            'data_create',
            'data',
            'genre',
            'info',
            'publisher',
            'image',
            'price',
            'like_count',
        ]

    @staticmethod
    def get_like_count(obj):
        return obj.like_set.all().count()


class LikeGameSerializers(serializers.ModelSerializer):
    class Meta:
        model = LikeGame
        fields = ['user', 'game']


#article
class ArticleSerializers(serializers.ModelSerializer):

    like_count = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'text',
            'image',
            'publish',
            'like_count',
            # 'tags',
        ]

    @staticmethod
    def get_like_count(obj):
        return obj.like_set.all().count()


class LikeArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'article']


#account
class AccountSerializers(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = [
                'id',
                'user',
                'date_of_birth',
                'avatar',
            ]


