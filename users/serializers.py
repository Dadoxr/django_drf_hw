from rest_framework.serializers import ModelSerializer
from edu.serializers import PaymentSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "pk",
            "first_name",
            "last_name",
            "email",
        ]


class UserListSerializer(ModelSerializer):
    payment = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "pk",
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "avatar",
            "payment",
        ]

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)

        if not (
            self.context["request"].user.is_superuser
            or self.context["request"].user.groups.filter(name="moderators").exists()
        ):
            fields.pop("avatar", None)
            fields.pop("first_name", None)
            fields.pop("avalast_nametar", None)
            fields.pop("payment", None)
            fields.pop("phone", None)

        return fields
