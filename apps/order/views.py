from django.shortcuts import render

def order_views(request):
    return render(request, 'order.html')
