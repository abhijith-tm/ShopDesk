from .models import Sale,SaleItem
from products.models import Product
from django.db import transaction
from rest_framework.exceptions import ValidationError

@transaction.atomic
def create_sale(validated_data):

    sale = Sale.objects.create(
               status = "pending"
    )
    for item in validated_data["items"]:
        product = item["product_id"]
        
      
        if item["quantity"] > product.stock_quantity:
            raise  ValidationError("Not enough stock")
        else:
            saleItem = SaleItem.objects.create( #also saves to db
                sale = sale,
                product = product,
                product_name = product.name,
                quantity = item["quantity"],
                unit_price = product.selling_price,
                cost_price = product.cost_price
            )
            #deduct stock
            product.stock_quantity -= item["quantity"]
            product.save() #save updated product quantity to db
    sale.status = "completed"
    sale.save()

    return sale




