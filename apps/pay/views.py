from django.shortcuts import render
import stripe
stripe.api_key = 'sk_test_51OziNsDWLasGw3aeMOZmHHfWWaB9lTAtQcm405e9NY0ighYv4wKN3t5uhem94g2Qzcs8tisFbgCXZulEyfGuouJ6005kbde5Im'

def pay_views(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=1000,
            currency='usd',
            description='xxx',
            source=request.POST['stripeToken']
        )
        if charge.status == 'succeeded':
            print('GOOD!')
    return render(request, 'pay.html')
