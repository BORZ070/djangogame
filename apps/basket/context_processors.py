from basket.models import Basket


def sample(request):
    try:
        user = request.user
        baskets = Basket.objects.filter(user=user)
        baskets_count = len(baskets)
    except:
        baskets_count = {}
    return{'baskets_total_count': baskets_count}
