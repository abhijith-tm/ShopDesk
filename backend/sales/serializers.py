from rest_framework import serializers
from .models import Sale
from products.models import Product

class SaleItemCreateSerializer(serializers.Serializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)


class SaleCreateSerializer(serializers.Serializer):
    items = SaleItemCreateSerializer(many=True)

#return a response to react after creating sale
class SaleCreateResponseSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Sale.objects.all())
    status = serializers.CharField()