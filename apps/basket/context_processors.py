from basket.models import Basket


def sample(request):
    user = request.user
    baskets = Basket.objects.filter(user=user)
    baskets_count = len(baskets)
    return{'baskets_total_count': baskets_count}
