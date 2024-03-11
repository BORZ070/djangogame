from django.shortcuts import render

from games.models import Favourite


def favorite_views(request):
    user = request.user
    favorites = Favourite.objects.filter(user=user)
    favorites_count = len(favorites)
    return render(request, 'favorite_index.html', {'user': user, 'favorites': favorites, 'favorites_count':favorites_count})
