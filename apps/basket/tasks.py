from django.core.cache import cache

from basket.models import Basket

from celery import shared_task


@shared_task()
def basket_signal(user_id):
    baskets = Basket.objects.filter(user=user_id)
    cache.set(f'baskets_{user_id}', baskets, timeout=None)

    baskets_count = len(baskets)
    cache.set(f'baskets_count_{user_id}', baskets_count, timeout=None)