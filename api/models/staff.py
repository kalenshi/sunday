from django.db import models

from api.models import Address
from api.models.store import Store


class Staff(models.Model):
	staff_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	address = models.ForeignKey(Address, models.DO_NOTHING)
	picture = models.TextField(blank=True, null=True)
	email = models.CharField(max_length=50, blank=True, null=True)
	store = models.ForeignKey(Store, models.DO_NOTHING)
	active = models.IntegerField()
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=40, db_collation="utf8mb4_bin", blank=True, null=True)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "staff"
