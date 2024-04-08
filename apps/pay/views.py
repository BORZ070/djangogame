from django.shortcuts import render, redirect
import stripe

from order.models import OrderItem

stripe.api_key = 'sk_test_51OziNsDWLasGw3aeMOZmHHfWWaB9lTAtQcm405e9NY0ighYv4wKN3t5uhem94g2Qzcs8tisFbgCXZulEyfGuouJ6005kbde5Im'


def pay_views(request):
    if request.method == 'POST':
        order_id = request.POST.get("order_id")
        order_items = OrderItem.objects.filter(order_number=order_id)
        total_sum = 0
        for order_item in order_items:
            game_price = order_item.game_price
            total_sum += game_price
        paying_sum = total_sum * 100


        charge = stripe.Charge.create(
            amount=paying_sum,
            currency='usd',
            description=f'paying order {order_id}',
            source=request.POST['stripeToken']
        )
        if charge.status == 'succeeded':
            print('GOOD!')
            for payed_item in order_items:
                payed_item.payed = True
                payed_item.save()
        return render(request, 'pay.html')
    else:
        return redirect('index_page')
