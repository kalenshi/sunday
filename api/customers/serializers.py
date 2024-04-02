from rest_framework import serializers

from api.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = (
			"customer_id",
			"first_name",
			"last_name",
			"email",
			"active",
			"create_date",
			"last_update",
			"store",
			"address"
		)
