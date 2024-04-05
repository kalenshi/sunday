from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status

from api.customers.list_view import CustomersList, CustomerPaginator
from api.models import Customer
from tests.factories import StoreFactory, AddressFactory
from tests.factories.customer_factory import CustomerFactory


class CustomerListViewTest(APITestCase):
	def setUp(self):
		self.view = CustomersList.as_view()
		self.factory = APIRequestFactory()
		self.store = StoreFactory()
		self.address = AddressFactory()
		self.user = get_user_model().objects.create_user(
			email="test@example.com", password="testpassword"
		)
		self.token = Token.objects.create(user=self.user)
		self.payload = {
			"first_name": "Kalenshi",
			"last_name": "Katebe",
			"email": "kalenshi@hotmail.com",
			"active": True,
			"store": self.store.store_id,
			"address": self.address.address_id
		}

	def test_paginated_list_view(self):
		_ = CustomerFactory.create_batch(size=10)
		request = self.factory.get('/customers/')
		force_authenticate(request, user=self.user, token=self.token)
		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_posting_a_new_customer_only_works_with_authenticated_users(self):
		"""Test you can create a customer"""

		request = self.factory.post('/customers/', data=self.payload)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_can_create_customer_when_authenticated(self):
		"""Test you can create a customer"""

		request = self.factory.post('/customers/', data=self.payload)
		force_authenticate(request, user=self.user, token=self.token)
		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
