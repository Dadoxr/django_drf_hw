from django.conf import settings
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from edu.models import Lesson
from edu.paginators import LessonCoursePagination
from edu.permissions import IsModerator, IsOwner
from edu.serializers import LessonSerializer
from edu.services import send_message_with_renew_course


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        [IsAuthenticated, ~IsModerator] if not settings.ALLOW_ANY_USER else [AllowAny]
    )


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        [IsAuthenticated, IsModerator | IsOwner]
        if not settings.ALLOW_ANY_USER
        else [AllowAny]
    )

    def put(self, request, *args, **kwargs):
        self.object = self.update(request, *args, **kwargs)
        send_message_with_renew_course.delay(self.object.pk)
        return self.object

    def patch(self, request, *args, **kwargs):
        self.object = self.update(request, *args, **kwargs)
        send_message_with_renew_course.delay(self.object.pk)
        return self.object


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        [IsAuthenticated, ~IsModerator | IsOwner]
        if not settings.ALLOW_ANY_USER
        else [AllowAny]
    )


class LessonRetrieveAPIView(generics.RetrieveAPIView):  # get
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        [IsAuthenticated, IsModerator | IsOwner]
        if not settings.ALLOW_ANY_USER
        else [AllowAny]
    )


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (
        [IsAuthenticated] if not settings.ALLOW_ANY_USER else [AllowAny]
    )
    pagination_class = LessonCoursePagination

    def get_queryset(self):
        queryset = super().get_queryset()
        if settings.ALLOW_ANY_USER:
            return queryset
        if (
            self.request.user.is_superuser
            or self.request.user.groups.filter(name="moderators").exists()
        ):
            return queryset

        return queryset.filter(owner=self.request.user)
