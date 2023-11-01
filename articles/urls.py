from django.urls import path

from articles.views import list_views, detail_views, like_articles_views


urlpatterns = [
    path('', list_views, name='article_all'),
    path('<int:pk>/', detail_views, name='article_detail'),
    path('like-articles/', like_articles_views, name='like_articles'),




]