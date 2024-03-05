from django.db import models

from api.models.address import Address


class Customer(models.Model):
	customer_id = models.SmallAutoField(primary_key=True)
	store = models.ForeignKey("Store", models.DO_NOTHING)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=50, blank=True, null=True)
	address = models.ForeignKey(Address, models.DO_NOTHING)
	active = models.IntegerField()
	create_date = models.DateTimeField()
	last_update = models.DateTimeField(blank=True, null=True)

	class Meta:
		app_label = "api"
		db_table = "customer"
