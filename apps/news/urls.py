from django.urls import path, include
from news.views import news_list

urlpatterns = [
    path('', news_list, name='news_list')



]