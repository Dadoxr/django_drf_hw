from django.contrib.auth.models import Group
from users.models import User
from django.core.management import BaseCommand
import os

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		
		all_user_email = {
			os.getenv('USER_EMAIL'): {'is_staff': False, 'is_superuser': False},
			os.getenv('STAFF_EMAIL'): {'is_staff': True, 'is_superuser': False},
			os.getenv('STAFF_SUPERUSER_EMAIL'): {'is_staff': True, 'is_superuser': True},
		}

		for email, values in all_user_email.items():
			user, just_created = User.objects.get_or_create(
				email=email,
				is_staff=values.get('is_staff', False),
				is_superuser=values.get('is_superuser', False),
			)
			user.set_password(os.getenv('SUPERUSER_STAFF_USER_PASSWORD'))
			user.save()

			moderators_group, just_created = Group.objects.get_or_create(name='moderators')
			if email == os.getenv('STAFF_EMAIL') and not user.groups.filter(name='moderators').exists():
				user.groups.add(moderators_group)
				user.save()
		
		