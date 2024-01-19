from django.urls import path

from blog.views import list_views, detail_views, edit_blog

urlpatterns = [
    path('', list_views, name='list_blog'),
    path('<int:pk>/', detail_views, name='detail_blog'),
    path('edit-blog/<int:pk>/', edit_blog, name='edit_blog'),



]