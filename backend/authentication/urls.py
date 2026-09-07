from django.urls import path
from .views import OwnerRegisterView, MeView, LogoutView

urlpatterns = [
    path('', OwnerRegisterView.as_view()),
    path('me/', MeView.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
]