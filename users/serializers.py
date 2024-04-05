from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		optional_fields = ("first_name", "last_name",)
		extra_kwargs = {
			"id": {"write_only": True},
			"password": {
				"write_only": True,
				"style": {"input_type": "password"}
			}
		}
