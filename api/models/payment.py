from django.db import models


class Payment(models.Model):
	payment_id = models.SmallAutoField(primary_key=True)
	customer = models.ForeignKey("Customer", models.DO_NOTHING, related_name="payments")
	staff = models.ForeignKey('Staff', models.DO_NOTHING)
	rental = models.ForeignKey("Rental", models.DO_NOTHING, blank=True, null=True)
	amount = models.DecimalField(max_digits=5, decimal_places=2)
	payment_date = models.DateTimeField()
	last_update = models.DateTimeField(blank=True, null=True)

	class Meta:
		app_label = "api"
		db_table = "payment"
