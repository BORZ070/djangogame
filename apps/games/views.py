from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render

from basket.models import Basket
from games.models import Like, Game, Favourite

from django.core.cache import cache


def list_views(request):
    games_with_like_count = Game.objects.annotate(like_count=Count('like'))
    return render(request, 'games_list_new.html', {'games_with_like_count': games_with_like_count})


def detail_views(request, pk):
    game = Game.objects.get(pk=pk)
    like_count = len(game.like_set.all())

    self_like = Like.objects.filter(user_id=request.user.id, game_id=pk).exists()
    if self_like:
        button_label = 'Unlike'
    else:
        button_label = 'Like'

    self_favourite = Favourite.objects.filter(user_id=request.user.id, game_id=pk).exists()
    if self_favourite:
        f_button_label = 'Unfavorite'
    else:
        f_button_label = 'Favorite'

    self_basket = Basket.objects.filter(user_id=request.user.id, game_id=pk).exists()
    if self_basket:
        bask_button_label = 'Unbasket'
    else:
        bask_button_label = 'Basket'

    return render(request, 'game_detail.html', {'game': game, 'like_count': like_count,
                                                'button_label': button_label, 'f_button_label': f_button_label,
                                                'bask_button_label': bask_button_label})


def like_game_views(request):
    user_id = request.POST.get('user_id')
    game_id = request.POST.get('game_id')

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


def basket_game_views(request):
    user_id = request.POST.get('user_id')
    game_id = request.POST.get('game_id')
    self_basket = Basket.objects.filter(user_id=user_id, game_id=game_id).exists()
    if self_basket:
        game_basket = Basket.objects.filter(user_id=user_id, game_id=game_id)
        game_basket.delete()
        bask_button_label = 'Basket'
    else:
        game_basket = Basket(user_id=user_id, game_id=game_id)
        game_basket.save()
        bask_button_label = 'Unbasket'

    return JsonResponse({'bask_button_label': bask_button_label})