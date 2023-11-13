from django.urls import path

from articles.views import list_views, detail_views, like_articles_views, favorite_articles_views, edit_article

urlpatterns = [
    path('', list_views, name='article_all'),
    path('<int:pk>/', detail_views, name='article_detail'),
    path('like-articles/', like_articles_views, name='like_articles'),
    path('favorite-articles/', favorite_articles_views, name='favorite_articles'),
    path('edit-article/<int:pk>/', edit_article, name='edit_article'),



]