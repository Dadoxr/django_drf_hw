from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="email", unique=True)
    confirmation_code = models.CharField(
        max_length=6, verbose_name="код подтверждения", blank=True, null=True
    )
    phone = models.IntegerField(verbose_name="телефон", null=True, blank=True)
    city = models.CharField(max_length=50, verbose_name="город", null=True, blank=True)
    avatar = models.ImageField(
        upload_to="users/", verbose_name="аватар", null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        verbose_name = "юзер"
        verbose_name_plural = "юзеры"
