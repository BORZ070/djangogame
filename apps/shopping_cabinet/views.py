from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from order.models import OrderItem, OrderNumber


@login_required
def cabinet_views(request):
    try:
        user = request.user
        orders = OrderNumber.objects.filter(user=user).order_by('-id')
    except:
        orders = {}
    return render(request, 'shopping_cabinet.html', {'orders': orders})

