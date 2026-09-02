from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    business = models.ForeignKey(
        "Business",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users"
    )


class Business(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)