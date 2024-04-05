from django.test import TestCase

from api.models import Customer
from tests.factories.customer_factory import CustomerFactory


class CustomerModelTest(TestCase):

	def test_create_customer(self):
		customer = CustomerFactory(
			first_name="MARIA",
			last_name="MILLER",
			email="MARIA.MILLER@sakilacustomer.org",
		)
		string = f"{customer.first_name} {customer.last_name}"
		self.assertEqual(1, Customer.objects.all().count())
		self.assertEqual(str(Customer.objects.first()), string)
