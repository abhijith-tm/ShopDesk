from django.urls import path

from .import views

urlpatterns = [
    path('',views.CreateSaleView.as_view()),
    path('cancel/<int:pk>/',views.CancelSaleView.as_view())
]