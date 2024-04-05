from django.db import models


class Inventory(models.Model):
	inventory_id = models.AutoField(primary_key=True)
	film = models.ForeignKey("Film", models.DO_NOTHING)
	store = models.ForeignKey("Store", models.DO_NOTHING)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "inventory"
