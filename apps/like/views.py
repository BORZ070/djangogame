from django.shortcuts import render

from django.core.cache import cache

from games.models import Like


def like_views(request):
    user = request.user

    likes = cache.get(f'likes_{user.id}')
    if not likes:
        likes = Like.objects.filter(user=user)
        cache.set(f'likes_{user.id}', likes, timeout=None)

    likes_count = cache.get(f'likes_count_{user.id}')
    if not likes_count:
        likes_count = len(likes)
        cache.set(f'likes_count_{user.id}', likes_count, timeout=None)

    return render(request, 'like_index.html', {'user': user, 'likes': likes, 'likes_count': likes_count})
