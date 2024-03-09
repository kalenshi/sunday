import time

from django.core.management.base import BaseCommand
from MySQLdb import OperationalError as MySQLOperationalError
from django.db.utils import OperationalError


class Command(BaseCommand):
	"""
	Command for waiting for mysql to load up before applying migrations
	"""
	def handle(self, *args, **options):
		connected = False
		while not connected:
			try:
				self.check(databases=["default"])
				connected = True
			except (MySQLOperationalError, OperationalError) as e:
				self.stdout.write(
					self.style.ERROR("Error connecting to. Sleeping for 1 second ...")
				)
				time.sleep(1)
		self.stdout.write(self.style.SUCCESS("DB Ready for connections ..."))
