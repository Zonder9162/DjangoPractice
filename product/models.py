from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)