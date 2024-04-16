from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.test import APIRequestFactory

from api.payment.list_view import PaymentListView
from tests.factories.paymnet_factory import PaymentFactory


class PaymentListViewTest(APITestCase):
	def setUp(self):
		self.factory = APIRequestFactory()
		self.view = PaymentListView().as_view()
		self.user = get_user_model().objects.create_user(
			email="test@example.com",
			password="strongpassword"
		)
		self.token = Token.objects.create(user=self.user)

	def test_get_lists_all_paginated_responses(self):
		_ = PaymentFactory.create_batch(size=100)
		request = self.factory.get('/payments/')
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["count"], 100)

	def test_wrong_payment_date_format(self):
		"""Test filtering on bad date format cause 400 response"""
		request = self.factory.get('/payments/?payment_date=2019/02/01')
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
