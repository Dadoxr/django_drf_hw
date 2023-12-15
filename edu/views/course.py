from rest_framework import status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from edu.models import Course, Subscription
from edu.paginators import LessonCoursePagination
from edu.permissions import IsModerator, IsAdmin, IsOwner
from edu.serializers import CourseSerializer
from users.models import User


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LessonCoursePagination

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


class SubscribeCourseAPIView(APIView):
    def post(self, request, user_pk, course_pk):
        user = get_object_or_404(User, pk=user_pk)
        course = get_object_or_404(Course, pk=course_pk)

        subscribe_on_course = Subscription.objects.filter(user=user, course=course)

        if subscribe_on_course.exists():
            return Response(
                {"detail": "Вы уже подписаны на этот курс"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        Subscription.objects.create(user=user, course=course)
        return Response(
            {"detail": "Подписка успешно установлена"}, status=status.HTTP_201_CREATED
        )


class UnsubscribeCourseAPIView(APIView):
    def delete(self, request, user_pk, course_pk):
        user = get_object_or_404(User, pk=user_pk)
        course = get_object_or_404(Course, pk=course_pk)

        subscribe_on_course = Subscription.objects.filter(user=user, course=course)

        if not subscribe_on_course.exists():
            return Response(
                {"detail": "Вы не подписаны на этот курс"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subscribe_on_course.first().delete()

        return Response(
            {"detail": "Подписка успешно отключена"}, status=status.HTTP_204_NO_CONTENT
        )
