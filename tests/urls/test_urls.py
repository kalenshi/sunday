"""
This test file is not needed, but I include just a few tests
for the purpose of learning url testing.
Anytime we write tests that don't involve database access, we use SimpleTestcase
"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse

from api.customers.list_view import CustomersListView


class TestUrls(SimpleTestCase):
	def test_customers_urls_resolve(self):
		"""Test customers list resolves to the correct view"""
		view, _, _ = resolve(reverse('api:customers-list'))
		self.assertEqual(view.cls, CustomersListView)
