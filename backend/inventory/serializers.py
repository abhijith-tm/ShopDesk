from rest_framework import serializers
from .models import InventoryAdjustment
class InventoryAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryAdjustment
        fields = ['business','product','quantity_changed','reason','performed_by','done_at']
        read_only_fields = ['performed_by','done_at']