from django.db import models


class Staff(models.Model):
	staff_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	address = models.ForeignKey(
		"Address", models.DO_NOTHING, related_name="staff"
	)
	picture = models.TextField(blank=True, null=True)
	email = models.CharField(max_length=50, blank=True, null=True)
	active = models.IntegerField()
	username = models.CharField(max_length=16)
	password = models.CharField(
		max_length=40, db_collation="utf8mb4_bin", blank=True, null=True
	)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "staff"
