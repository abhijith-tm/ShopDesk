from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import InventoryAdjustment
from .serializers import InventoryAdjustmentSerializer
from permissions.permission import CanAdjustInventory
from .services import create_inventory_adjustment
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class InventoryAdjustmentListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,CanAdjustInventory]
    queryset = InventoryAdjustment.objects.all()
    serializer_class = InventoryAdjustmentSerializer

    def perform_create(self, serializer):
        create_inventory_adjustment(
        serializer.validated_data,
        self.request.user
        )