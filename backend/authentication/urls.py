from django.urls import path
from .views import OwnerRegisterView

urlpatterns = [
    path('', OwnerRegisterView.as_view()),
]