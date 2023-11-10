from django.conf import settings
from django.db import models
from django.urls import reverse

from games.models import Game


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='title_article')
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.pk])


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='like_user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.article}'


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_user')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.article}'


