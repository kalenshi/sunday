import datetime

import factory

from api.models import Staff


class StaffFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Staff
		django_get_or_create = ("address",)

	address = factory.SubFactory("tests.factories.address_factory.AddressFactory")
	last_update = datetime.datetime.now(datetime.UTC)
	active = True
