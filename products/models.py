from django.db import models
from rest_framework.fields import DateTimeField
from Inventory_jg_1.core.models import BaseModel

class Category(BaseModel):
    name = models.CharField

class Item(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    height = models.FloatField(null=True,blank=True)
    width = models.FloatField(null=True,blank=True)
    length = models.FloatField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    category = models.ManyToOneRel(Category, on_delete=models.CASCADE, related_name='items')
    stock_qty = models.PositiveIntegerField
    expiration_date = DateTimeField(null=True,blank=True)

