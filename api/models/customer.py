from django.db import models

from api.models.address import Address


class Customer(models.Model):
	customer_id = models.SmallAutoField(primary_key=True)
	store = models.ForeignKey("Store", default=1, on_delete=models.DO_NOTHING)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.CharField(max_length=50, blank=True, null=True)
	address = models.ForeignKey(Address, models.DO_NOTHING)
	active = models.BooleanField(default=True)
	create_date = models.DateTimeField(auto_now_add=True)
	last_update = models.DateTimeField(blank=True, null=True)

	class Meta:
		app_label = "api"
		db_table = "customer"

	def __str__(self):
		"""
		String representation of the customer model
		Returns:
			str: String representation of the customer
		"""
		return f"{self.first_name} {self.last_name}"
