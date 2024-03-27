from django.conf import settings
from django.db import models

from games.models import Game


class OrderNumber(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    user_name = models.CharField(max_length=50)
    user_id_int = models.IntegerField()

    def __str__(self):
        return f'{self.id}'


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.PROTECT, blank=True, null=True)
    game_name = models.CharField(max_length=50)
    game_price = models.IntegerField()
    order_number = models.ForeignKey(OrderNumber, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.user} - {self.game}'
