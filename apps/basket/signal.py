from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from basket.tasks import basket_signal
from basket.models import Basket


@receiver(post_save, sender=Basket)
def basket_cache_update(instance, **kwargs):
    basket_signal.delay(instance.user.id)


@receiver(post_delete, sender=Basket)
def basket_cache_update(instance, **kwargs):
    basket_signal.delay(instance.user.id)