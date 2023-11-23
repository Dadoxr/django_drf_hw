from rest_framework.serializers import ModelSerializer
from edu.serializers import PaymentSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "avatar",
        ]


class UserListSerializer(ModelSerializer):
    payment = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "avatar",
            
            "payment",
        ]
