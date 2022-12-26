from django.db import models

class Give(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    numberItems = models.IntegerField(default=0)
    giver = models.CharField(max_length=120)
    date = models.DateField(auto_created=True)
    inStock = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title

