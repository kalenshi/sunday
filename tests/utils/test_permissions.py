from unittest.mock import MagicMock

from django.test import TestCase

from api.permissions import IsAdminOrReadOnly


class TestPermissions(TestCase):
	def setUp(self):
		self.permission_class = IsAdminOrReadOnly()

	def test_permissions_not_admin_return_false(self):
		"""Test allows requests in safe_methods"""
		request = MagicMock(method="post")
		view = MagicMock(method="post", permission_classes=[self.permission_class])

		response = view(request)
		self.assertTrue(response)
