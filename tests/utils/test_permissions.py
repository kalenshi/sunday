from unittest.mock import MagicMock

from django.contrib.auth import get_user_model
from django.test import TestCase

from api.permissions import IsAdminOrReadOnly


class TestPermissions(TestCase):
	def setUp(self):
		self.permission_class = IsAdminOrReadOnly()
		self.super_user = get_user_model().objects.create_superuser(
			email="test@example.com",
			password="strongpassword",
			company="testcompany"
		)
		self.regular_user = get_user_model().objects.create_user(
			email="test2@example.com",
			password="password",
			company="testcompany2"
		)

	def test_permissions_returns_true_in_safe_methods(self):
		"""Test allows requests in safe_methods"""
		request = MagicMock(method="GET", user=self.regular_user)
		view = MagicMock(method="GET")
		self.assertTrue(
			self.permission_class.has_object_permission(request=request, view=view, obj=None)
		)

	def test_permissions_returns_true_in_non_safe_methods_for_super_user(self):
		request = MagicMock(method="POST", user=self.super_user)
		view = MagicMock(method="POST")

		self.assertTrue(
			self.permission_class.has_object_permission(request=request, view=view, obj=None)
		)
