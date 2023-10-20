from django.conf import settings
from django.db import models
from games.models import Game


class Article(models.Model):
    title = models.CharField(max_length=50)

    text = models.TextField()
    image = models.ImageField(upload_to='title_article')


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_user')
    game = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.game}'