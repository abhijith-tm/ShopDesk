from django.urls import path
from .views import OwnerRegisterView, MeView

urlpatterns = [
    path('', OwnerRegisterView.as_view()),
    path('me/', MeView.as_view()),

]