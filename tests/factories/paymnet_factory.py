import factory
from factory import fuzzy
import datetime
from django.utils import timezone

from api.models import Payment


class PaymentFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Payment

	customer = factory.SubFactory("tests.factories.customer_factory.CustomerFactory")
	staff = factory.SubFactory("tests.factories.staff_factory.StaffFactory")
	rental = factory.SubFactory("tests.factories.rental_factory.RentalFactory")
	last_update = datetime.datetime.now(datetime.UTC)
	amount = fuzzy.FuzzyDecimal(0.5, 12, 2)
	payment_date = fuzzy.FuzzyDateTime(
		datetime.datetime(2008, 1, 1, tzinfo=timezone.utc),
		datetime.datetime(2012, 1, 1, tzinfo=timezone.utc)
	)
