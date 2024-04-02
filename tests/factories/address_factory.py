import datetime
import factory

from api.models import Address


class AddressFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Address

	last_update = datetime.datetime.now(datetime.UTC)
	city = factory.SubFactory("tests.factories.city_factory.CityFactory")
