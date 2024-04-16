from django.test import TestCase
from rest_framework import serializers

from users.models import User
from users.serializers import UserSerializer


class UserSerializerTest(TestCase):
	"""Test User Serializer validation works"""

	def setUp(self):
		self.serializer = UserSerializer
		self.payload = {
			"email": "test@example.com",
			"password": "password",
			"password1": "password",
			"company": "testcompany"
		}

	def test_validate_password_works(self):
		data = {
			"email": "test@example.com",
			"password": "password",
			"password1": "password1",
		}

		with self.assertRaises(serializers.ValidationError) as err:
			serializer = self.serializer(data=data)
			_ = serializer.validate(attrs=data)

		self.assertEqual(
			err.exception.detail[0], "Passwords don't match"
		)

	def test_validation_returns_the_attrs(self):
		serializer = self.serializer(data=self.payload)
		self.assertEqual(serializer.is_valid(), True)

	def test_create__method_creates_a_new_user(self):
		"""Test the create method creates a new user instance in the database"""
		serializer = self.serializer(data=self.payload)
		serializer.is_valid()
		user = serializer.save()
		self.assertIsInstance(user, User)
		self.assertEqual(User.objects.count(), 1)

	def test_update__method_updates_a_user(self):
		payload = {
			"email": "test@example.com",
			"password": "password",
			"company": "testcompany"
		}
		user = User.objects.create_user(**payload)
		self.assertTrue(user.check_password("password"))
		self.assertEqual(user.email, payload["email"])
		update_payload = {
			"password": "newpassword"
		}
		user = self.serializer().update(instance=user, validated_data=update_payload)
		# ensure the password has been updated but not the email
		self.assertTrue(user.check_password("newpassword"))
		self.assertEqual(user.email, payload["email"])
