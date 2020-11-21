from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    """Table for adding ingredient"""
    name = models.CharField(max_length=100, null=False)
    quantity = models.IntegerField(null=False, default=0)
    cost_price = models.DecimalField(max_digits=5, decimal_places=3, null=False, default=0.0)
    selling_price = models.DecimalField(max_digits=5, decimal_places=3, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    """Table for adding a new product"""
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class ProductIngredient(models.Model):
    """Product to ingredient and vice-versa mapping"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


class Transaction(models.Model):
    """Maintains customer orders."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    billed_amount = models.DecimalField(max_digits=5, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)





