from .models import Business
from models import User
from django.contrib.auth.models import Group
def create_owner(self, validated_data):
    business_name = validated_data.pop("business_name")
    password = validated_data.pop("password")
    email = validated_data.pop("email")

    business = Business.objects.create(name=business_name)

    user = User.objects.create_user(
        username=email,
        email=email,
        password=password,
        first_name=validated_data["first_name"],
        business=business,
    )

    owner_group = Group.objects.get(name="Owner")
    user.groups.add(owner_group)

    return user