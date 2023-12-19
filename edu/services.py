
from django.conf import settings
from edu.models import Lesson
from users.models import User
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_message_with_renew_course(pk):
    lesson = Lesson.objects.get(pk=pk)
    subscribe_users = User.objects.filter(subscriptions__course=lesson.course)

    for user in subscribe_users:
        send_mail(
            "Обновление курса",
            f"Курс {lesson.title} был обновлен",
            settings.EMAIL_HOST,
            [user.email,],
            fail_silently=False,
        )
