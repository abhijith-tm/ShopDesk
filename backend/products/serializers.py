from rest_framework import serializers

from .models import Product

#DRF serializers convert complex Python/Django objects to native Python data types 
# and validate/convert incoming data back into native Python data types. 
# Renderers then turn that representation into JSON.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','cost_price','selling_price','stock_quantity','created_at','updated_at']
        read_only_fields = ['id','created_at','updated_at'] #prevents write
        
