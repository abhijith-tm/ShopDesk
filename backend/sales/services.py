from .models import Sale, SaleItem
from django.db import transaction
from rest_framework.exceptions import ValidationError
from django.utils import timezone


@transaction.atomic
def create_sale(validated_data, user):

    sale = Sale.objects.create(
        status="pending",
        business=user.business
    )

    for item in validated_data["items"]:
        product = item["product_id"]

        # Make sure the product belongs to the user's business
        if product.business != user.business:
            raise ValidationError(
                "Product does not belong to your business."
            )

        if item["quantity"] > product.stock_quantity:
            raise ValidationError("Not enough stock")

        sale_item = SaleItem.objects.create(
            sale=sale,
            product=product,
            product_name=product.name,
            quantity=item["quantity"],
            unit_price=product.selling_price,
            cost_price=product.cost_price
        )

        # Deduct stock
        product.stock_quantity -= item["quantity"]
        product.save()

    sale.status = "completed"
    sale.save()

    return sale


@transaction.atomic
def cancel_sale(sale_id, reason, user):

    sale = Sale.objects.get(
        id=sale_id,
        business=user.business
    )

    if sale.status == "cancelled":
        raise ValidationError("Sale is already cancelled.")

    elif sale.status == "completed":
        for item in sale.items.all():
            product = item.product

            product.stock_quantity += item.quantity
            product.save()

    sale.status = "cancelled"
    sale.cancel_reason = reason
    sale.cancelled_by = user
    sale.cancelled_at = timezone.now()

    sale.save()

    return sale