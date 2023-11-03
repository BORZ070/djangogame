from django.db.models import Count
from django.shortcuts import render, redirect
from articles.models import Article,Like
from django.http import JsonResponse


def list_views(request):
    articles_with_like_count = Article.objects.annotate(like_count=Count('like'))

    return render(request, 'articles.html', {'articles_with_like_count':articles_with_like_count})

def detail_views(request, pk):
    article = Article.objects.get(pk=pk)
    like_count = len(article.like_set.all())
    return render(request,'article.html', {'article':article, 'like_count':like_count})

def like_articles_views(request):

    user_id = request.POST.get('user_id')
    article_id = request.POST.get('article_id')

    self_like = Like.objects.filter(user_id=user_id, article_id=article_id).exists()
    if self_like:
        article_like = Like.objects.filter(user_id=user_id, article_id=article_id)
        article_like.delete()
    else:
        article_like = Like(user_id=user_id, article_id=article_id)
        article_like.save()

    like_count = Article.objects.get(id=article_id).like_set.count()

    return JsonResponse({'like_count':like_count})