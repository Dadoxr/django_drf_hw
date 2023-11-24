from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from edu.models import Course
from edu.permissions import IsModerator, IsAdmin, IsOwner
from edu.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        permission_classes = [IsAuthenticated]

        if self.action in ("create", "destroy"):
            permission_classes.append(IsAdmin)
        elif self.action in ("update"):
            permission_classes.append(IsAdmin | IsOwner | IsModerator)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = super().get_queryset()

        if (
            self.request.user.is_superuser
            or self.request.user.groups.filter(name="moderators").exists()
        ):
            return queryset

        return queryset.filter(owner=self.request.user)
