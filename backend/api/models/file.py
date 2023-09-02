from django.db import models


class File(models.Model):
    filename = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    hash = models.CharField(max_length=32)