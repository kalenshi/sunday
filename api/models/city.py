from django.db import models


class City(models.Model):
	city_id = models.SmallAutoField(primary_key=True)
	city = models.CharField(max_length=50)
	country = models.ForeignKey("Country", models.DO_NOTHING)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "city"
