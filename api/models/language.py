from django.db import models


class Language(models.Model):
	language_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=20)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "language"
