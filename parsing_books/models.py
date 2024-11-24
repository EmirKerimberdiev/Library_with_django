from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=900)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title
