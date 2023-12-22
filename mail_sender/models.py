from django.db import models

class MailForAllUser(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
