
from rest_framework.routers import DefaultRouter
from users.apps import UsersConfig
from django.urls import path

from users.serializers import UserSerializer


app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserSerializer, basename='users')

urlpatterns = [

] + router.urls