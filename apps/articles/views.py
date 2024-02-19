from django.db.models import Count
from django.shortcuts import render, redirect
from articles.models import Article, Like, Favorite
from django.http import JsonResponse
from articles.forms import ArticleEditForm

from django.core.paginator import Paginator

from django.core.cache import cache


def list_views(request):
    articles = Article.objects.annotate(like_count=Count('like'))
    articles_with_like_count_list = articles.filter(publish=True)
    #paginator
    paginator = Paginator(articles_with_like_count_list, 2)
    page_number = request.GET.get('page', 1)
    articles_with_like_count = paginator.page(page_number)
    return render(request, 'articles_new.html', {'articles_with_like_count':articles_with_like_count})


def detail_views(request, pk):
    article = Article.objects.get(pk=pk)

    like_count = cache.get('like_count')
    if not like_count:

        like_count = len(article.like_set.all())
        cache.set('like_count', like_count)

    self_like = cache.get('self_like')
    if not self_like:

        self_like = Like.objects.filter(user_id=request.user.id, article_id=pk).exists()
        if self_like:
            button_label = 'Unlike'
        else:
            button_label = 'Like'

    self_favorite = cache.get('self_favorite')
    if not self_favorite:

        self_favorite = Favorite.objects.filter(user_id=request.user.id, article_id=pk).exists()
        if self_favorite:
            f_button_label = 'Unfavorite'
        else:
            f_button_label = 'Favorite'

    return render(request,'article.html', {'article':article, 'like_count':like_count, 'button_label':button_label, 'f_button_label':f_button_label})


def like_articles_views(request):
    user_id = request.POST.get('user_id')
    article_id = request.POST.get('article_id')

    self_like = cache.get('self_like')
    if not self_like:

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

    self_favorite = cache.get('self_favorite')
    if not self_favorite:

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


def edit_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        form = ArticleEditForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
    else:
        form = ArticleEditForm(instance=article)

    return render(request, 'edit_article.html', {'form':form, 'article':article})


