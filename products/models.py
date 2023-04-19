from django.db import models
from django.utils import timezone


class Category(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Product(models.Model):
    name = models.CharField(max_length=255)
    stock = models.IntegerField()
    ranking = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
