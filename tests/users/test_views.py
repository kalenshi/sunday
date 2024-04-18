from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.views import CreateUserView


class TestUserView(APITestCase):
	def setUp(self):
		self.factory = APIRequestFactory()
		self.view = CreateUserView().as_view()
		self.user = get_user_model().objects.create_superuser(
			email="test@example.cpom",
			password="strong_password",
			company="sunday"
		)
		self.token = Token.objects.create(user=self.user)

	def test_user_creation_post_endpoint(self):
		payload = {
			"email": "test@example.com",
			"password": "strong_password",
			"password1": "strong_password",
			"first_name": "testfirst",
			"last_name": "testlast",
			"company": "testcompany",
		}
		request = self.factory.post("/users/create/", payload)
		force_authenticate(request, user=self.user)
		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_user_creation_put_endpoint_bad_request(self):
		payload = {
			"email": "test@example.com",
			"password": "strong_password",
			"first_name": "testfirst",
			"last_name": "testlast",
			"company": "testcompany",
		}
		request = self.factory.post("/users/create/", payload)
		force_authenticate(request, user=self.user)
		response = self.view(request)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
