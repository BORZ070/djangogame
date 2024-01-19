from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image = models.ImageField(upload_to='title_blog')
    data = models.CharField(max_length=50)

    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     return reverse('detail_blog', args=[self.pk])



