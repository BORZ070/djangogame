from django.db.models import Count
from django.shortcuts import render, redirect
from articles.models import Article, Like, Favorite
from django.http import JsonResponse


def list_views(request):
    articles_with_like_count = Article.objects.annotate(like_count=Count('like'))

    return render(request, 'articles.html', {'articles_with_like_count':articles_with_like_count})

def detail_views(request, pk):

    article = Article.objects.get(pk=pk)
    like_count = len(article.like_set.all())

    self_like = Like.objects.filter(user_id=request.user.id, article_id=pk).exists()
    if self_like:
        button_label = 'Unlike'
    else:
        button_label = 'Like'

    self_favorite = Favorite.objects.filter(user_id=request.user.id, article_id=pk).exists()
    if self_favorite:
        f_button_label = 'Unfavorite'
    else:
        f_button_label = 'Favorite'

    return render(request,'article.html', {'article':article, 'like_count':like_count, 'button_label':button_label, 'f_button_label':f_button_label})

def like_articles_views(request):

    user_id = request.POST.get('user_id')
    article_id = request.POST.get('article_id')

    self_like = Like.objects.filter(user_id=user_id, article_id=article_id).exists()
    if self_like:
        article_like = Like.objects.filter(user_id=user_id, article_id=article_id)
        article_like.delete()
        button_label = 'Like'
    else:
        article_like = Like(user_id=user_id, article_id=article_id)
        article_like.save()
        button_label = 'Unlike'

    like_count = Article.objects.get(id=article_id).like_set.count()

    return JsonResponse({'like_count':like_count, 'button_label':button_label})


def favorite_articles_views(request):

    user_id = request.POST.get('user_id')
    article_id = request.POST.get('article_id')

    self_favorite = Favorite.objects.filter(user_id=user_id, article_id=article_id).exists()
    if self_favorite:
        article_favorite = Favorite.objects.filter(user_id=user_id, article_id=article_id)
        article_favorite.delete()
        f_button_label = 'Favorite'
    else:
        article_favorite = Favorite(user_id=user_id, article_id=article_id)
        article_favorite.save()
        f_button_label = 'Unfavorire'

    return JsonResponse({'f_button_label':f_button_label})