from unittest.mock import patch, MagicMock
from django.test import TestCase
from rest_framework import serializers

from users.serializers import TokenSerializer


class TokenSerializerTest(TestCase):
	def setUp(self):
		self.serializer = TokenSerializer()

	def test_token_serializer_validation_error(self):
		with self.assertRaises(serializers.ValidationError) as err:
			_ = TokenSerializer().validate(
				attrs={"email": "test@example.com", "password": "some_password"}
			)
		self.assertEqual(
			str(err.exception.detail[0]),
			"Unable to Authenticate with provided credentials"
		)

	@patch("users.serializers.authenticate")
	def test_token_serializer_validation_success(self, patched_authenticate):
		user = MagicMock(email="test@example.com", password="test_password")
		patched_authenticate.return_value = user
		attrs = self.serializer.validate(
			attrs={"email": "test@example.com", "password": "test_password"}
		)

		self.assertEqual(attrs["user"], user)
