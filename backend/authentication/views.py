from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import OwnerRegisterSerializer
from .services import create_owner


class OwnerRegisterView(CreateAPIView):
    serializer_class = OwnerRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = create_owner(serializer.validated_data)

        return Response(
            {
                "message": "Owner registered successfully",
                "user_id": user.id,
                "email": user.email,
            },
            status=status.HTTP_201_CREATED
        )