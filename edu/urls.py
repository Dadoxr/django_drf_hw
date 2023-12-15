from django.urls import path
from rest_framework.routers import DefaultRouter
from edu.apps import EduConfig
from edu.views.course import (
    CourseViewSet,
    SubscribeCourseAPIView,
    UnsubscribeCourseAPIView,
)
from edu.views.lesson import (
    LessonCreateAPIView,
    LessonListAPIView,
    LessonDestroyAPIView,
    LessonUpdateAPIView,
    LessonRetrieveAPIView,
)
from edu.views.payment import PaymentListAPIView

app_name = EduConfig.name

course_router = DefaultRouter()
course_router.register(
    prefix=r"course",
    viewset=CourseViewSet,
    basename="course",
)

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/list/", LessonListAPIView.as_view(), name="lesson_list"),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path("lesson/get/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_get"),
    path("payment/list/", PaymentListAPIView.as_view(), name="payment_list"),
    path(
        "courses/<int:user_pk>/<int:course_pk>/subscribe/",
        SubscribeCourseAPIView.as_view(),
        name="subscribe_course",
    ),
    path(
        "courses/<int:user_pk>/<int:course_pk>/unsubscribe/",
        UnsubscribeCourseAPIView.as_view(),
        name="unsubscribe_course",
    ),
] + course_router.urls
