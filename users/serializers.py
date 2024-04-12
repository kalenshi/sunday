from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import (
	get_user_model, authenticate
)
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
	password1 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = get_user_model()
		fields = (
			"email",
			"first_name",
			"last_name",
			"company",
			"password",
			"password1"
		)
		optional_fields = ("first_name", "last_name",)
		extra_kwargs = {
			"id": {"write_only": True}
		}
		validators = [
			UniqueTogetherValidator(
				queryset=get_user_model().objects.all(),
				message=_("Must have unique users from the same company"),
				fields=["email", "company"]
			)
		]

	def validate(self, attrs):
		password = attrs.get("password")
		password1 = attrs.get("password1")
		if password != password1:
			raise serializers.ValidationError(_("Passwords don't match"), code="password_mismatch")
		return attrs

	def create(self, validated_data):
		validated_data.pop("password1")
		return get_user_model().objects.create_user(**validated_data)

	def update(self, instance, validated_data):
		"""Update and return instance"""
		password = validated_data.pop("password", None)
		user = super().update(instance, validated_data)
		if password is not None:
			user.set_password(password)
			user.save()
		return user


class TokenSerializer(serializers.Serializer):
	"""Serializer for the user auth model"""
	email = serializers.EmailField()
	password = serializers.CharField(
		style={"input_type": "password"},
		trim_whitespace=False
	)

	def validate(self, attrs):
		email = attrs.get("email")
		password = attrs.get("password")
		user = authenticate(
			request=self.context.get("request"),
			username=email,
			password=password,
		)
		if not user:
			msg = _("Unable to Authenticate with provided credentials")
			raise serializers.ValidationError(msg, code="authentication")
		attrs['user'] = user
		return attrs
