from django.shortcuts import render
import pickle

def news_list(request):
    with open('news_dump', 'rb') as file:
        data = pickle.load(file)
    news_all = data['articles']

    return render(request, 'news_list.html', {'news_all': news_all})
