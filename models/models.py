from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    """Table for adding ingredient"""
    name = models.CharField(max_length=100, null=False)
    quantity = models.IntegerField(null=False, default=0)
    cost_price = models.DecimalField(null=False, default=0.0)
    selling_price = models.DecimalField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_add=True, null=False)


class Product(models.Model):
    """Table for adding a new product"""
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class ProductIngredient(models.Model):
    """Product to ingredient and vice-versa mapping"""
    product = models.ForeignKey(Product)
    ingredient = models.ForeignKey(Ingredient)


class Transaction(models.Model):
    """Maintains customer orders."""
    product = models.ForeignKey(Product)
    billed_amount = models.DecimalField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # payment_status = models.ChoiceField(choices=PAYMENT_CHOICES)
    customer = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_add=True, null=False)





