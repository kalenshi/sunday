from django.db import models


class Country(models.Model):
	country_id = models.SmallAutoField(primary_key=True)
	country = models.CharField(max_length=50)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "country"

	def __str__(self):
		"""
		Returns the country name as a string
		Returns:
			str: country name
		"""
		return self.country
