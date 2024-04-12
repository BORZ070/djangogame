from django.shortcuts import render

from order.models import OrderItem, OrderNumber


def cabinet_views(request):
    user = request.user
    orders = OrderNumber.objects.filter(user=user).order_by('-id')
    return render(request, 'shopping_cabinet.html', {'orders':orders})

