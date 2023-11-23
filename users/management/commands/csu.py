from users.models import User
from django.core.management import BaseCommand

class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		user = User.objects.create(
			email='admin@admin.ru',
			is_staff=True,
			is_superuser=True
		)
		user.set_password('1234')
		user.save()