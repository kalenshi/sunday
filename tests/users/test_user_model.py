from django.test import TestCase

from users.models import User


class UserModelTest(TestCase):
	def test_can_create_a_regular_user(self):
		"""Test creating a regular user with no superuser status"""
		user = User.objects.create_user(
			email="test@example.com",
			password="strongpassword",
			company="testcompany"
		)
		self.assertFalse(user.is_superuser)

	def test_can_create_a_superuser(self):
		user = User.objects.create_superuser(
			email="test@example.com",
			password="strongpassword",
			company="testcompany"
		)
		self.assertTrue(user.is_superuser)

	def test_user_model_raises_value_error_without_email(self):
		with self.assertRaises(ValueError) as err:
			_ = User.objects.create_user(
				email='', password='testpassword', company="testcompany"
			)
		self.assertEqual(str(err.exception), 'Email is required')

	def test_string_representation_works(self):
		user = User.objects.create_user(
			email='test@example.com', password='testpassword', company="testcompany",
		)
		self.assertEqual(str(user), user.email)
