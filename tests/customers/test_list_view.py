from unittest.mock import patch

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory
from rest_framework import status

from api.customers.list_view import CustomersList, CustomerPaginator
from api.models import Customer
from tests.factories.customer_factory import CustomerFactory


class CustomerListViewTest(APITestCase):
	def setUp(self):
		self.view = CustomersList.as_view()
		self.factory = APIRequestFactory()
		self.client = APIClient()

	# def test_paginated_list_view(self):
	# 	# create customers
	# 	_ = CustomerFactory.create_batch(size=10)
	# 	request = self.factory.get('/customers/')
	# 	response = self.view(request)
	#
	# 	self.assertEqual(response.status_code, status.HTTP_200_OK)
