from django.db import models
from rest_framework.fields import DateTimeField


class Category(models.Model):
    name = models.CharField

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    height = models.FloatField(null=True, blank=True)
    width = models.FloatField(null=True, blank=True)
    length = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    stock_qty = models.PositiveIntegerField()
    expiration_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
