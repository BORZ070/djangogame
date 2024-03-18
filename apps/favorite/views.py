from django.shortcuts import render

from games.models import Favourite

from django.core.cache import cache


def favorite_views(request):
    user = request.user

    favorites = cache.get(f'favorites_{user.id}')
    if not favorites:
        favorites = Favourite.objects.filter(user=user)
        cache.set(f'favorites_{user.id}', favorites, timeout=None)

    favorites_count = cache.get(f'favorites_count_{user.id}')
    if not favorites_count:
        favorites_count = len(favorites)
        cache.set(f'favorites_count_{user.id}', favorites_count, timeout=None)

    return render(request, 'favorite_index.html', {'user': user, 'favorites': favorites, 'favorites_count': favorites_count})
