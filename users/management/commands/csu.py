from users.models import User, UserRoleChoices
from django.core.management import BaseCommand
import os

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		all_user_email = {
			os.getenv('USER_EMAIL'): {'is_staff': False, 'is_superuser': False, 'role': UserRoleChoices.MEMBER},
			os.getenv('STAFF_EMAIL'): {'is_staff': True, 'is_superuser': False, 'role': UserRoleChoices.MODERATOR},
			os.getenv('STAFF_SUPERUSER_EMAIL'): {'is_staff': True, 'is_superuser': True, 'role': UserRoleChoices.MODERATOR},
		}

		for email, values in all_user_email.items():
			user = User.objects.create(
				email=email,
				is_staff=values.get('is_staff', False),
				is_superuser=values.get('is_superuser', False),
				role=values.get('role', UserRoleChoices.MEMBER)
			)
			user.set_password(os.getenv('SUPERUSER_STAFF_USER_PASSWORD'))
			user.save()
		