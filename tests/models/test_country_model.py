from tests.factories.country_factory import CountryFactory
from api.models import Country

from django.test import TestCase


class TestCountryModel(TestCase):
	def setUp(self):
		self.country = CountryFactory(country="Zambia")

	def test_country_str(self):
		self.assertEqual(str(Country.objects.first()), "Zambia")
