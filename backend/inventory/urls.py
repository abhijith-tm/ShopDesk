from django.urls import path

from .import views

urlpatterns = [
    path('',views.InventoryAdjustmentListCreateView.as_view())
]