from django.db import models

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(default=000000000)
    sexe = models.CharField(max_length=1, default='M')

    def __str__(self) -> str:
        return self.name

class Entr(models.Model):
    name = models.CharField(max_length=100)
    chief = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return self.name