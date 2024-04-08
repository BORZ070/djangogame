from django.shortcuts import render, redirect

from basket.models import Basket
from order.models import OrderNumber, OrderItem


def order_views(request):
    user = request.user
    items = Basket.objects.filter(user=user)
    if len(items) != 0:
        new_order_number = OrderNumber(user=user, user_name=user.username, user_id_int=user.id)
        new_order_number.save()
        for basket_object in items:
            game = basket_object.game
            new_order = OrderItem(user=user, game=game, game_name=game.name, game_price=game.price,
                                  order_number=new_order_number)
            new_order.save()
        items.delete()
        order_items = OrderItem.objects.filter(order_number=new_order_number)

        total_sum = 0
        for order_item in order_items:
            game_price = order_item.game_price
            total_sum += game_price

        paying_sum = total_sum * 100
        return render(request, 'order.html', {'new_order_number': new_order_number, 'order_items': order_items, 'total_sum': total_sum, 'paying_sum': paying_sum})
    else:
        return redirect('basket')
