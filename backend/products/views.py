#view is a Python function or class that receives a web request and returns a web response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .models import Product

# /api/products/  Get ->list all. POST-> create

class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#/api/products/<id>/  GET    → retrieve one , PUT    → update, PATCH  → partial update,  DELETE → delete
class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
