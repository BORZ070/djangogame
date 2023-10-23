from django.db.models import Count
from django.shortcuts import render
from articles.models import Article


def list_views(request):
    articles_with_like_count = Article.objects.annotate(like_count=Count('like'))

    return render(request, 'articles.html', {'articles_with_like_count':articles_with_like_count})

def detail_views(request, pk):
    article = Article.objects.get(pk=pk)
    like_count = len(article.like_set.all())
    return render(request,'article.html', {'article':article, 'like_count':like_count})