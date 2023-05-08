from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

	def handle(self, *args, **options):
		# Check if a user record with the username 'awsadmin' exists in the database
		# If it does not exist, then create a super-user with that username,
		# Supply an email address and a password to it
		# So, now we have an admin user to manage our AWS RDS database
		if not User.objects.filter(username="admin").exists():
			User.objects.create_superuser("admin", "ellie93kim@gmail.com", "admin123")