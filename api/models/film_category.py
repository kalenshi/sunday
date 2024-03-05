from django.db import models

from api.models.category import Category
from api.models.film import Film


class FilmCategory(models.Model):
	# The composite primary key (film_id, category_id) found,
	# that is not supported. The first column is selected.
	film = models.OneToOneField(Film, models.DO_NOTHING, primary_key=True)
	category = models.ForeignKey(Category, models.DO_NOTHING)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "film_category"
		unique_together = (("film", "category"),)
