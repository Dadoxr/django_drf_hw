from rest_framework import generics, viewsets
from edu.permissions import IsAdmin, IsModerator
from users.models import User
from users.serializers import UserSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    http_method_names = ["put", "patch"]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        if self.action in ("create", "update", "destroy"):
            permission_classes.append(IsAdmin | IsModerator)
        return [permission() for permission in permission_classes]
