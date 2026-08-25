from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import Sale
from .serializers import SaleCreateSerializer,SaleCreateResponseSerializer
from .services import create_sale
from rest_framework import status
from rest_framework.response import Response

class CreateSaleView(CreateAPIView):
    queryset = Sale.objects.all() #without this generic view will throw error when stock is less
    serializer_class = SaleCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sale = create_sale(serializer.validated_data)

        response_serializer = SaleCreateResponseSerializer(sale)

        return Response(
            response_serializer.data,
            status = status.HTTP_201_CREATED
        )