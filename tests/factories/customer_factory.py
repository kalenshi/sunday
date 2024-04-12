import datetime

import factory

from api.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Customer

	email = factory.Sequence(lambda n: f"example{n}@test.com")
	address = factory.SubFactory("tests.factories.address_factory.AddressFactory")
	active = True
	last_update = datetime.datetime.now(datetime.UTC)
	store = factory.SubFactory("tests.factories.store_factory.StoreFactory")
