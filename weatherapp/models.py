from django.db import models
from datetime import datetime


class City(models.Model):
    time = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
