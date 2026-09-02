from rest_framework import serializers
from .services import create_owner


class OwnerRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    business_name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return create_owner(**validated_data)