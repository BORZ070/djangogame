from django.conf import settings
from django.db import models

class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class Publisher(models.Model):
    publisher = models.CharField(max_length=50)

    def __str__(self):
        return self.publisher

class Game(models.Model):
    data_create = models.DateTimeField(auto_now_add=True)
    data = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='game_main')
    price = models.IntegerField()
    # tag

    def __str__(self):
        return self.name

class Platform(models.Model):
    platform = models.CharField(max_length=50)
    game = models.ManyToManyField(Game, related_name='game_platform')

    def __str__(self):
        return self.platform


class Favourite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_favorite')

    def __str__(self):
        return f'{self.user} - {self.game}'


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.game}'