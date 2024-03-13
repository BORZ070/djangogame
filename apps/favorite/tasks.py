from django.core.cache import cache

from games.models import Favourite

from celery import shared_task


@shared_task()
def favorite_signal(user_id):
    favorites = Favourite.objects.filter(user=user_id)
    cache.set(f'favorites_{user_id}', favorites, timeout=None)

    favorites_count = len(favorites)
    cache.set(f'favorites_count_{user_id}', favorites_count, timeout=None)