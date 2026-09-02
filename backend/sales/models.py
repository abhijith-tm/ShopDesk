from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator
from django.db.models import Q
from authentication.models import Business

# Create your models here.

class Sale(models.Model):

    class Status(models.TextChoices):
      PENDING = 'pending'
      COMPLETED = 'completed'
      CANCELLED = 'cancelled'

    class Users(models.TextChoices):
          EMPLOYEE = 'Employee'
          MANAGER = 'Manager'
          OWNER = 'Owner'

    business = models.ForeignKey(
        to=Business, 
        on_delete=models.PROTECT ,
    )

    status = models.CharField(
       max_length=9,
       choices=Status.choices,
       default=Status.PENDING
    )

    created_at = models.DateTimeField(
       auto_now_add=True
    )
    
    cancelled_at = models.DateTimeField(
        null=True,
	)

    cancelled_by = models.CharField(
        max_length=20,
        choices=Users.choices,
        null=True
	)

    cancel_reason = models.CharField(
        null=True,
        max_length=200
	)

class SaleItem(models.Model):
	sale = models.ForeignKey(
		to=Sale, 
		on_delete=models.CASCADE # saleItem gets deleted when sale gets deleted
		,related_name="items" # so we can do sale.items.all() instead of sale.saleitem_set.all()
	)

	product = models.ForeignKey(
		to=Product,
		on_delete=models.PROTECT #prevents delete

	)

	product_name = models.CharField(
	max_length=200,

	)

	quantity = models.IntegerField(
		default=1,
		validators=[MinValueValidator(1)]
	)

	unit_price = models.DecimalField(
		max_digits=8,
		decimal_places=2,
		validators=[MinValueValidator(0)]
	)

	cost_price = models.DecimalField(
		max_digits=8,
		decimal_places=2,
		validators=[MinValueValidator(0)]
	)
	class Meta:
          constraints = [
              models.CheckConstraint(
                condition=Q(quantity__gte=1),
				name="quantity_gteater_than_1"
			  ),
 			  models.CheckConstraint(
				condition=Q(unit_price__gte=0),
				name="unit_price_gteater_than_0"
			  ),
     		  models.CheckConstraint(
					condition=Q(cost_price__gte=0),
					name="cost_price_gteater_than_0 "
			  )
		  ]