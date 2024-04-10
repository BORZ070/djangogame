from django.shortcuts import render

from order.models import OrderItem, OrderNumber


def cabinet_views(request):
    user = request.user
    all_user_order_item = OrderItem.objects.filter(user=user)
    all_user_order_number = OrderNumber.objects.filter(user=user)
    item_for_number = all_user_order_number.ordernumber.all()
    return render(request, 'shopping_cabinet.html', {'all_user_order_number': all_user_order_number,
                                                     'item_for_number': item_for_number})
