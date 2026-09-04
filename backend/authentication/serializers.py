from rest_framework import serializers
from .models import User

class OwnerRegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    business = serializers.CharField(max_length=200)

class UserDetailsSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(source="business.name")
    role = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "business_name",
            "role",
        ]

    
    def get_role(self, obj):
        group = obj.groups.first()
        return group.name if group else None