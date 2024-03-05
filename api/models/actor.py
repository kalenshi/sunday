from django.db import models


class Actor(models.Model):
	actor_id = models.SmallAutoField(primary_key=True)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "actor"
