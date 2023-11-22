from django.urls import path
from rest_framework.routers import DefaultRouter
from edu.apps import EduConfig
from edu.views.course import CourseViewSet
from edu.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonDestroyAPIView, LessonUpdateAPIView, LessonRetrieveAPIView

app_name = EduConfig.name

course_router = DefaultRouter()
course_router.register(prefix=r"course", viewset=CourseViewSet, basename='course',)

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='create_lesson'),
    path('lesson/list/', LessonListAPIView.as_view(), name='list_lesson'),

    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='delete_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='update_lesson'),
    path('lesson/get/<int:pk>/', LessonRetrieveAPIView.as_view(), name='get_lesson'),

] + course_router.urls