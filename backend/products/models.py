from django.db import models
from django.core.validators import MinValueValidator

from django.db.models import Q

# Create your models here.

class Product(models.Model):
    # id = models.CharField() // djnago Django automatically adds a primary-key field if you don't define one.
    name = models.CharField(max_length=200)
    cost_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)] #prevent -ve value

    )

    selling_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    stock_quantity = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [ #gives database level integrity - cant change database values to negative
            models.CheckConstraint(
                condition=Q(selling_price__gte=0),
                name="selling_price_non_negative"
            ), 
            models.CheckConstraint(
                condition=Q(cost_price__gte=0),
                name="cost_price_non_negative",
            ),
            models.CheckConstraint(
                condition=Q(stock_quantity__gte=0),
                name="stock_quantity_non_negative",
            ),]