
from django.conf import settings
from django.utils.timezone import now, timedelta
from users.models import User
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_message_with_renew_course():
    subscribe_users = User.objects.filter(subscriptions__isnull=False)
    for user in subscribe_users:
        subscriptions = user.subscriptions.all()
        for subscription in subscriptions:
            course = subscription.course
            if course.last_change > now() - timedelta(days=1):
                send_mail(
                    "Обновление курса",
                    f"Курс {course.title} был обновлен",
                    settings.EMAIL_HOST,
                    [user.email,],
                    fail_silently=False,
                )

send_message_with_renew_course.delay()