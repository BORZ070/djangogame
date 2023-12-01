from django.contrib.auth.models import User
from django.db import models
from games.models import Genre


class TbotUserProfile(models.Model):
    tuser_id = models.IntegerField(unique=True)
    tuser_name = models.CharField(max_length=200, blank=True, null=True)
    tuser_first_name = models.CharField(max_length=200, blank=True, null=True)
    tuser_preference_genre = models.ForeignKey(Genre, on_delete=models.PROTECT, blank=True, null=True)
    tspam = models.BooleanField(default=True)
    tuser_link_to_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.tuser_name}, {self.tuser_link_to_user}'


class SupportQ(models.Model):
    email = models.EmailField()
    data = models.DateField(auto_now=True)
    question = models.TextField()

    def __str__(self):
        return f'{self.data},{self.email}'