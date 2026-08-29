from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# Create your models here.

class InventoryAdjustment(models.Model):

    product = models.ForeignKey(
        to=Product, 
        on_delete=models.PROTECT ,
        related_name="inventory_adjustments"
    )

    quantity_changed = models.IntegerField()

    reason = models.CharField(
        max_length=200
    )

    performed_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="inventory_adjustments"
    )

    done_at = models.DateTimeField(
        auto_now_add=True
    )