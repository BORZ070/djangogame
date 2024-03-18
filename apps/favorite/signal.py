from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from favorite.tasks import favorite_signal
from games.models import Favourite


@receiver(post_save, sender=Favourite)
def favorite_cache_update(instance, **kwargs):
    favorite_signal.delay(instance.user.id)


@receiver(post_delete, sender=Favourite)
def favorite_cache_update(instance, **kwargs):
    favorite_signal.delay(instance.user.id)
