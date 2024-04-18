import factory
from factory import fuzzy
import datetime
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.test import APIRequestFactory

from api.payment.list_view import PaymentListView
from api.models import Payment
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

	@patch("api.models.Payment.objects.select_related")
	@patch("api.payment.list_view.json")
	def test_list_view_filters(self, json_patch, related_patch):
		"""Test filtering on payment date format cause 200 response"""
		payments = PaymentFactory.create_batch(
			size=10,
			payment_date=fuzzy.FuzzyDateTime(
				datetime.datetime(2018, 11, 1, tzinfo=timezone.utc),
				datetime.datetime(2024, 11, 1, tzinfo=timezone.utc)
			)
		)
		payments.append(
			PaymentFactory.create(
				payment_date=datetime.datetime(2019, 11, 1, tzinfo=timezone.utc)
			)
		)

		related_patch.return_value = Payment.objects.all()
		json_patch.dumps.return_value = {"count": len(payments)}
		request = self.factory.get("/payments/?payment_date=2019-11-1")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(related_patch.assert_called_once)
		self.assertEqual(response.data["count"], 1)

	@patch("api.payment.list_view.cache")
	def test_list_view_no_cache_response(self, patched_cache):
		patched_cache.get.return_value = None
		request = self.factory.get("/payments/")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(patched_cache.get.called)
		self.assertTrue(patched_cache.set.called)

	@patch("api.payment.list_view.cache")
	def test_list_view_cached_response(self, patched_cache):
		""""
		Test cached response works
		"""
		payments = PaymentFactory.create_batch(size=10)
		patched_cache.get.return_value = payments
		request = self.factory.get("/payments/")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertTrue(patched_cache.get.called)
		self.assertFalse(patched_cache.set.called)
