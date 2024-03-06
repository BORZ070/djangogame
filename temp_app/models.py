from django.db import models

class TableOne(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True)


class TableTwo(models.Model):
    table = models.ForeignKey(TableOne, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True)