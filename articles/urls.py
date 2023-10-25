from django.urls import path

from articles.views import list_views, detail_views


urlpatterns = [
    path('', list_views, name='article_all'),
    path('<int:pk>/', detail_views, name='article_detail')





]