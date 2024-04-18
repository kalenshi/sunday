from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):
	def create_user(
		self,
		email,
		first_name=None,
		last_name=None,
		password=None,
		**extra_fields):
		"""
		Creates and saves a user with the given email and password
		Args:
			first_name:
			last_name:
			email:
			password:
			**extra_fields:

		Returns:

		"""
		if not email:
			raise ValueError('Email is required')
		user = self.model(
			first_name=first_name,
			last_name=last_name,
			email=self.normalize_email(email),
			**extra_fields
		)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(
		self,
		email,
		first_name=None,
		last_name=None,
		password=None,
		**extra_fields):
		"""

		Args:
			first_name:
			last_name:
			email:
			password:
			**extra_fields:

		Returns:

		"""
		user = self.create_user(
			first_name=first_name,
			last_name=last_name,
			email=email,
			password=password,
			**extra_fields
		)
		user.is_superuser = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user


class User(AbstractBaseUser, PermissionsMixin):
	"""
	Custom user Model which supports using email instead of username
	"""
	first_name = models.CharField(
		max_length=100, verbose_name="First Name", null=True, blank=True
	)
	last_name = models.CharField(
		max_length=100, verbose_name="Last Name", null=True, blank=True
	)
	email = models.EmailField(max_length=255, unique=True, verbose_name="Email")
	company = models.CharField(max_length=255, verbose_name="Organization")

	is_active = models.BooleanField(default=True, verbose_name="Is Active")
	is_superuser = models.BooleanField(default=False, verbose_name="Is Admin")
	is_staff = models.BooleanField(default=False, verbose_name="Is Staff")

	objects = UserManager()

	USERNAME_FIELD = "email"

	REQUIRED_FIELDS = ["company", ]

	def __str__(self):
		"""String representation of the user model"""
		return f"{self.email}"

	class Meta:
		app_label = "users"
		managed = True
