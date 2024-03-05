from django.db import models


class FilmText(models.Model):
	film_id = models.PositiveSmallIntegerField(primary_key=True)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)

	class Meta:
		app_label = "api"
		db_table = "film_text"
