from rest_framework import serializers
from games.models import Game
from articles.models import Article



class GameSerializers(serializers.ModelSerializer):
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
            'price'
        ]


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'text',
            'image',
            'publish',
            # 'tags',
        ]

