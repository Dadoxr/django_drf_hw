from django.utils.timezone import now, timedelta
from users.models import User
from celery import shared_task

@shared_task
def block_users():
    inactive_threshold = now() - timedelta(days=31)
    users_to_block = User.objects.filter(last_login__lt=inactive_threshold)
    
    for user in users_to_block:
        user.is_active = False
    
    User.objects.bulk_update(users_to_block)

        