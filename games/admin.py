from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from  games.models import Game, Genre, Publisher
@admin.register(Game)
class GameAdmin(SummernoteModelAdmin):
     list_display = ('name', 'genre', 'data',)
     summernote_fields = '__all__'
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
     list_display = ('genre',)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
     list_display = ('publisher',)


