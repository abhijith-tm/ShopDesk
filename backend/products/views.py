#view is a Python function or class that receives a web request and returns a web response

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from permissions.permission import CanModifyProducts
# /api/products/  Get ->list all. POST-> create

class ProductListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,CanModifyProducts]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(business=self.request.user.business)

    def get_queryset(self):
        return Product.objects.filter(
        business=self.request.user.business
        )

#/api/products/<id>/  GET    → retrieve one , PUT    → update, PATCH  → partial update,  DELETE → delete
class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,CanModifyProducts]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
