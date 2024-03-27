from django.shortcuts import render

from basket.models import Basket
from order.models import OrderNumber, OrderItem


def order_views(request):
    user = request.user
    items = Basket.objects.filter(user=user)
    new_order_number = OrderNumber(user=user, user_name=user.username, user_id_int=user.id)
    new_order_number.save()
    for basket_object in items:
        game = basket_object.game
        new_order = OrderItem(user=user, game=game, game_name=game.name, game_price=game.price,
                              order_number=new_order_number)
        new_order.save()

    return render(request, 'order.html')
