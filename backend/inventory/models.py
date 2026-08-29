from django.db import models
from products.models import Product
# Create your models here.

class Inventory(models.Model):

    product = models.ForeignKey(
        to=Product, 
        on_delete=models.CASCADE ,
        related_name="items"
    )

    quantity = models.IntegerField()

    reason = models.CharField(
        max_length=200
    )

    perfomed_by = models.CharField(
        max_length=10
    )

    done_at = models.DateTimeField()