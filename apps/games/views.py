from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from games.models import Like, Game, Favourite

from django.core.cache import cache


def list_views(request):
    games_with_like_count = Game.objects.annotate(like_count=Count('like'))

    return render(request, 'games_list_new.html', {'games_with_like_count': games_with_like_count})


def detail_views(request, pk):
    game = Game.objects.get(pk=pk)

    like_count = cache.get('like_count')
    if not like_count:
        like_count = len(game.like_set.all())
        cache.set('like_count', like_count, timeout=None)

    self_like = cache.get('self_like')
    if not self_like:
        self_like = Like.objects.filter(user_id=request.user.id, game_id=pk).exists()
        cache.set('self_like', self_like, timeout=None)

    if self_like:
        button_label = 'Unlike'
    else:
        button_label = 'Like'

    self_favorite = cache.get('self_favorite')
    if not self_favorite:

        self_favourite = Favourite.objects.filter(user_id=request.user.id, game_id=pk).exists()
        if self_favourite:
            f_button_label = 'Unfavorite'
        else:
            f_button_label = 'Favorite'

    return render(request,'game_detail.html', {'game': game, 'like_count': like_count, 'button_label': button_label, 'f_button_label': f_button_label})


def like_game_views(request):
    user_id = request.POST.get('user_id')
    game_id = request.POST.get('game_id')

    self_like = cache.get('self_like')
    if not self_like:

        self_like = Like.objects.filter(user_id=user_id, game_id=game_id).exists()
        if self_like:
            game_like = Like.objects.filter(user_id=user_id, game_id=game_id)
            game_like.delete()
            button_label = 'Like'
        else:
            game_like = Like(user_id=user_id, game_id=game_id)
            game_like.save()
            button_label = 'Unlike'

    like_count = Game.objects.get(id=game_id).like_set.count()

    return JsonResponse({'like_count': like_count, 'button_label': button_label})


def favourite_game_views(request):
    user_id = request.POST.get('user_id')
    game_id = request.POST.get('game_id')

    self_favorite = cache.get('self_favorite')
    if not self_favorite:

        self_favourite = Favourite.objects.filter(user_id=user_id, game_id=game_id).exists()
        if self_favourite:
            game_favourite = Favourite.objects.filter(user_id=user_id, game_id=game_id)
            game_favourite.delete()
            f_button_label = 'Favorite'
        else:
            game_favourite = Favourite(user_id=user_id, game_id=game_id)
            game_favourite.save()
            f_button_label = 'Unfavorire'

    return JsonResponse({'f_button_label': f_button_label})
