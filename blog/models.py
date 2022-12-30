from django.db import models


class realisation(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=None)
    entr = models.CharField(max_length=150, null=None, default=None)
    thumb = models.ImageField(upload_to='realisation', blank=True, null=True)

    def __str__(self):
        return self.title