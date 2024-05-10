import random
import string
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/', blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True, null=True)
    registered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

    def get_uuid_url(self):
        return reverse('uuid_validater', args=[self.uuid])


class ReferralCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            for _ in range(10):
                self.code = self.generate_code()
                try:
                    super().save(*args, **kwargs)
                    break
                except:
                    continue


    @staticmethod
    def generate_code():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
