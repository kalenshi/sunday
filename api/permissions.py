from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
	"""
	Custom permissions to only allow admins to edit or create
	new instances of our objects
	"""

	def has_object_permission(self, request, view, obj):
		"""
		Custom permission to only allow Admins to create new instances of our objects
		Args:
			request:
			view:
			obj:

		Returns:

		"""
		if request.method in permissions.SAFE_METHODS:
			return True
		return request.user.is_staff
