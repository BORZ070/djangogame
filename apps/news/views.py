from django.shortcuts import render
import pickle
from django.core.cache import cache


def news_list(request):
    news_all = cache.get('news_all')
    if not news_all:
        with open('news_dump', 'rb') as file:
            data = pickle.load(file)
        news_all = data['articles'][:6]
        cache.set('news_all', news_all, timeout=3600)
    return render(request, 'news_list.html', {'news_all': news_all})
