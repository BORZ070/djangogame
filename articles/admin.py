from django.contrib import admin
from articles.models import Article, Like, Favorite
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Article)
class ArticleAdmin(SummernoteModelAdmin):
    list_display = ('title','text',)
    summernote_fields = '__all__'


admin.site.register(Like)
admin.site.register(Favorite)






