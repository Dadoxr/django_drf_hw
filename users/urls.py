
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from django.urls import path

from users.views import UserListAPIView, UserViewSet


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('list/', UserListAPIView.as_view(), name='users_list'),
] + router.urls

