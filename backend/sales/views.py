from django.shortcuts import render
from rest_framework.generics import CreateAPIView,UpdateAPIView
from .models import Sale
from .serializers import SaleCreateSerializer,SaleCreateResponseSerializer,SaleCancelSerializer,SaleCancelResponseSerializer
from .services import create_sale,cancel_sale
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from permissions.permission import CanModifyProducts,CanModifySale
class CreateSaleView(CreateAPIView):
    queryset = Sale.objects.all() #without this generic view will throw error when stock is less
    serializer_class = SaleCreateSerializer

    def create(self, request, *args, **kwargs): #overiding
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sale = create_sale(serializer.validated_data,request.user)

        response_serializer = SaleCreateResponseSerializer(sale)

        # return Response({ #testing jwt
        #     "username": request.user.username,
        #     "is_employee": request.user.groups.filter(name="Employee").exists(),
        #     "is_manager": request.user.groups.filter(name="Manager").exists(),
        #     "is_owner": request.user.groups.filter(name="Owner").exists(),
        #     })
        return Response(
            response_serializer.data,
            status = status.HTTP_201_CREATED,
        )

class CancelSaleView(UpdateAPIView):
    permission_classes = [IsAuthenticated,CanModifySale]
    queryset = Sale.objects.all()
    serializer_class = SaleCancelSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        pk = self.kwargs.get("pk")

        sale = cancel_sale(pk,serializer.validated_data["cancel_reason"],"not implemented")

        response_serializer = SaleCancelResponseSerializer(sale)

        return Response(
            response_serializer.data,
            status = status.HTTP_200_OK
        )