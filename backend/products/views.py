#view is a Python function or class that receives a web request and returns a web response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from sales.permission import CanModifyProducts
# /api/products/  Get ->list all. POST-> create

class ProductListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,CanModifyProducts]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#/api/products/<id>/  GET    → retrieve one , PUT    → update, PATCH  → partial update,  DELETE → delete
class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,CanModifyProducts]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
