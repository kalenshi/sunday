from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase, force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status

from tests.factories import CustomerFactory
from api.customers.detail_view import CustomerDetailView


class TestCustomerDetailView(APITestCase):
	def setUp(self):
		self.factory = APIRequestFactory()
		self.view = CustomerDetailView().as_view()
		self.customer = CustomerFactory(
			first_name='Kalenshi',
			last_name='Katebe',
			email='test@example.com'
		)
		self.user = get_user_model().objects.create_user(
			email="test@example.cpom",
			password="strong_password",
			company="sunday"
		)
		self.token = Token.objects.create(user=self.user)

	def test_can_retrieve_a_customer_detail_by_id(self):
		payload = {"customer_id": self.customer.customer_id}
		request = self.factory.get("/api/customers/")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request, **payload)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data["email"], self.customer.email)

	def test_can_delete_a_customer_detail_by_id(self):
		"""
		Test that a customer can be deleted by setting a customer
		active status to false
		"""
		payload = {"customer_id": self.customer.customer_id}
		self.customer.active = True
		request = self.factory.delete("/api/customers")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request, **payload)

		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.customer.refresh_from_db()
		self.assertFalse(self.customer.active)

	def test_can_patch_a_customer_active_status_by_id(self):
		"""
		Test that a customer can have their email updated correctly
		"""
		self.customer.active = False

		payload = {"active": 1}
		request = self.factory.patch("/api/customers/", payload, format="json")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request, self.customer.customer_id)

		self.assertEqual(response.status_code, status.HTTP_206_PARTIAL_CONTENT)
		self.customer.refresh_from_db()
		self.assertTrue(self.customer.active)

	def test_can_patch_customer_email_by_id(self):
		"""
		Test that a customer can change their existing email as long as it's not taken
		"""
		payload = {"email": "test2@example.com"}
		request = self.factory.patch("/api/customers", payload, format="json")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request, self.customer.customer_id)

		self.assertEqual(response.status_code, status.HTTP_206_PARTIAL_CONTENT)
		self.customer.refresh_from_db()
		self.assertEqual(self.customer.email, "test2@example.com")

	def test_patch_a_customer_email_fails_when_email_exists(self):
		"""
		Test that changing a customers email fails when the email is already taken by
		another customer
		"""
		_ = CustomerFactory.create(email="taken@example.com")
		payload = {"email": "taken@example.com"}
		request = self.factory.patch("/api/customers/", payload, format="json")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request, self.customer.customer_id)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_patch_bad_request(self):
		"""
		Tests patching with bad data return bad request response
		"""
		request = self.factory.patch("/api/customers", {"active": 10}, format="json")
		force_authenticate(request, user=self.user, token=self.token.key)
		response = self.view(request, self.customer.customer_id)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
