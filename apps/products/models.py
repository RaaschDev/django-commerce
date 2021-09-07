from django.db import models


class ProductCategory(models.Model):
    name = models.CharField("name", max_length=155)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Name", max_length=155)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.PROTECT, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name
