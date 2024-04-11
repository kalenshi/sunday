import factory
import datetime

from api.models import Inventory


class InventoryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Inventory

	last_update = datetime.datetime.now(datetime.UTC)
	film = factory.SubFactory("tests.factories.film_factory.FilmFactory")
	store = factory.SubFactory("tests.factories.store_factory.StoreFactory")
