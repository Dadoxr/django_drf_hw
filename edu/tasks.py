
from django.conf import settings
from edu.models import Course
from users.models import User
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_message_with_renew_course(course_id: int) -> None:
    course = Course.objects.get(pk=course_id)

    subscribers = course.subscribed_users.all()

    send_mail(
        subject='Обновление курса',
        message=f'Курс "{course.title}" был обновлен',
        from_email=settings.EMAIL_HOST,
        recipient_list=subscribers.values_list('email', flat=True),
        fail_silently=False,
    )