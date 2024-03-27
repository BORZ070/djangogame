from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render, redirect

from basket.models import Basket
from games.models import Game


def basket_views(request):
    user = request.user

    baskets = cache.get(f'baskets_{user.id}')
    if not baskets:
        baskets = Basket.objects.filter(user=user)
        cache.set(f'baskets{user.id}', baskets, timeout=None)

    baskets_count = cache.get(f'baskets_count_{user.id}')
    if not baskets_count:
        baskets_count = len(baskets)
        cache.set(f'baskets_count_{user.id}', baskets_count, timeout=None)

    total_sum = 0
    for basket in baskets:
        game_price = basket.game.price
        total_sum += game_price

    return render(request, 'basket.html', {'user': user, 'baskets': baskets, 'baskets_count': baskets_count, 'total_sum':total_sum})


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


# def basket_button(request, pk):
#     self_basket = Basket.objects.filter(user_id=request.user.id, game_id=pk).exists()
#     if self_basket:
#         bask_button_label = 'Unbasket'
#     else:
#         bask_button_label = 'Basket'
#     return render(request, 'game_detail.html', {'bask_button_label': bask_button_label})


def basket_clearing(request):
    user_id = request.POST.get('user_id')
    game_id = request.POST.get('game_id')
    if game_id:
        game_basket = Basket.objects.filter(user_id=user_id, game_id=game_id)
        game_basket.delete()
    else:
        game_basket = Basket.objects.filter(user_id=user_id)
        game_basket.delete()

    return redirect('basket')

