# from django.core.cache import cache
#
# from games.models import Favourite
#
#
# def favorite_signal(user):
#     favorites = Favourite.objects.filter(user=user)
#     cache.set(f'favorites_{user.id}', favorites, timeout=None)
#
#     favorites_count = len(favorites)
#     cache.set(f'favorites_count_{user.id}', favorites_count, timeout=None)