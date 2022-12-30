from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Entr(models.Model):
    name = models.CharField(max_length=100)
    chief = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumb = models.ImageField(upload_to='user', blank=True, null=True)

    def __str__(self) -> str:
        return self.name
