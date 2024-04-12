import factory
from factory import fuzzy
import datetime
from django.utils import timezone

from api.models import Rental


class RentalFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Rental

	inventory = factory.SubFactory("tests.factories.inventory_factory.InventoryFactory")
	customer = factory.SubFactory("tests.factories.customer_factory.CustomerFactory")
	staff = factory.SubFactory("tests.factories.staff_factory.StaffFactory")
	last_update = datetime.datetime.now(datetime.UTC)
	rental_date = fuzzy.FuzzyDateTime(
		datetime.datetime(2008, 1, 1, tzinfo=timezone.utc),
		datetime.datetime(2012, 1, 1, tzinfo=timezone.utc)
	)
