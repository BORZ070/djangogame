from django.core.cache import cache

from games.models import Like

from celery import shared_task


@shared_task()
def like_signal(user_id):
    likes = Like.objects.filter(user=user_id)
    cache.set(f'likes_{user_id}', likes, timeout=None)

    likes_count = len(likes)
    cache.set(f'likes_count_{user_id}', likes_count, timeout=None)