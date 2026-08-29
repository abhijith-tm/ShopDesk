from .models import InventoryAdjustment
from products.models import Product
from django.db import transaction
from rest_framework.exceptions import ValidationError

@transaction.atomic
def create_inventory_adjustment(validated_data,user):

        product = validated_data["product"]
        
      
        if (validated_data["quantity_changed"] + product.stock_quantity ) < 0: # so that product quantity wont become -ve
            raise  ValidationError("Not enough stock to reduce")
        else:
            inventory_adjustment= InventoryAdjustment.objects.create( #also saves to db
                product = product,
                quantity_changed = validated_data["quantity_changed"],
                reason = validated_data["reason"],
                performed_by = user
            )

         #stock calculation
        product.stock_quantity += validated_data["quantity_changed"]
        product.save() #save updated product quantity to db
        return inventory_adjustment