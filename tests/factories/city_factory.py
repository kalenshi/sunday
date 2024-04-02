import datetime
import factory

from api.models import City


class CityFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = City

	last_update = datetime.datetime.now(datetime.timezone.utc)
	country = factory.SubFactory("tests.factories.country_factory.CountryFactory")
