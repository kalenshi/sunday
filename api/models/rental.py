from django.db import models


class Rental(models.Model):
	rental_id = models.AutoField(primary_key=True)
	rental_date = models.DateTimeField()
	inventory = models.ForeignKey("Inventory", models.DO_NOTHING)
	customer = models.ForeignKey("Customer", models.DO_NOTHING)
	return_date = models.DateTimeField(blank=True, null=True)
	staff = models.ForeignKey("Staff", models.DO_NOTHING)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "rental"
		unique_together = (("rental_date", "inventory", "customer"),)
