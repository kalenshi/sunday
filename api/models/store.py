from django.db import models

from api.models import Address


class Store(models.Model):
	store_id = models.AutoField(primary_key=True)
	manager_staff = models.OneToOneField("Staff", models.DO_NOTHING, related_name="manages")
	address = models.ForeignKey(Address, models.DO_NOTHING)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "store"
