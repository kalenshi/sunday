import datetime
import factory

from api.models import Country


class CountryFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Country

	last_update = datetime.datetime.now(datetime.UTC)
