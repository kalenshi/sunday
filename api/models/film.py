from django.db import models


class Film(models.Model):
	film_id = models.SmallAutoField(primary_key=True)
	title = models.CharField(max_length=128)
	description = models.TextField(blank=True, null=True)
	release_year = models.TextField(blank=True, null=True)  # This field type is a guess.
	language = models.ForeignKey("Language", models.DO_NOTHING)
	original_language = models.ForeignKey(
		"Language", models.DO_NOTHING,
		related_name="film_original_language_set",
		blank=True,
		null=True
	)
	rental_duration = models.PositiveIntegerField()
	rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
	length = models.PositiveSmallIntegerField(blank=True, null=True)
	replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
	rating = models.CharField(max_length=5, blank=True, null=True)
	special_features = models.CharField(max_length=54, blank=True, null=True)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "film"
