from django.db import models


class Address(models.Model):
	address_id = models.SmallAutoField(primary_key=True)
	address = models.CharField(max_length=50)
	address2 = models.CharField(max_length=50, blank=True, null=True)
	district = models.CharField(max_length=20)
	city = models.ForeignKey('City', models.DO_NOTHING)
	postal_code = models.CharField(max_length=10, blank=True, null=True)
	phone = models.CharField(max_length=20)
	location = models.TextField()  # This field type is a guess.
	last_update = models.DateTimeField()

	class Meta:
		app_label = 'api'
		db_table = 'address'
