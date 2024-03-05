from django.db import models

from api.models.actor import Actor
from api.models.film import Film


class FilmActor(models.Model):
	# The composite primary key (actor_id, film_id) found,
	# that is not supported. The first column is selected.
	actor = models.OneToOneField(Actor, models.DO_NOTHING, primary_key=True)

	film = models.ForeignKey(Film, models.DO_NOTHING)
	last_update = models.DateTimeField()

	class Meta:
		app_label = "api"
		db_table = "film_actor"
		unique_together = (("actor", "film"),)
