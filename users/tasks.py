from django.utils.timezone import now, timedelta
from users.models import User

def block_user(pk=None):
    if pk:
        try:
            user = User.objects.get(pk=pk)
            user.is_active = False
            user.save()
        except User.DoesNotExist:
            pass
    else:
        inactive_threshold = now() - timedelta(days=31)
        users_to_block = User.objects.filter(last_login__lt=inactive_threshold)
        
        for user in users_to_block:
            user.is_active = False
            user.save()

        