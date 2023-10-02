from django.contrib import admin
from  games.models import Game, Genre, Publisher
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
     list_display = ('name', 'genre', 'data',)
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
     list_display = ('genre',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
     list_display = ('publisher',)