from django.db import models


class Minecraft(models.Model):
    version = models.CharField(max_length=128)
    hash = models.CharField(max_length=32)
    # @TODO: libraries