import datetime
import factory

from api.models import Store


class StoreFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Store

	address = factory.SubFactory("tests.factories.address_factory.AddressFactory")
	manager_staff = factory.SubFactory("tests.factories.staff_factory.StaffFactory")
	last_update = datetime.datetime.now(datetime.UTC)
