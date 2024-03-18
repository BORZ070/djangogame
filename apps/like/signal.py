from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from like.tasks import like_signal
from games.models import Like


@receiver(post_save, sender=Like)
def like_cache_update(instance, **kwargs):
    like_signal.delay(instance.user.id)


@receiver(post_delete, sender=Like)
def like_cache_update(instance, **kwargs):
    like_signal.delay(instance.user.id)