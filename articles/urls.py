from django.urls import path

from articles.views import list_views

urlpatterns = [
    path('', list_views, name='article_all')






]