from rest_framework import serializers

from api.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'


# {
# 	"customer_id": 1,
# 	"first_name": "MARY",
# 	"last_name": "SMITH",
# 	"email": "MARY.SMITH@sakilacustomer.org",
# 	"active": 1,
# 	"create_date": "2006-02-14T22:04:36Z",
# 	"last_update": "2006-02-15T04:57:20Z",
# 	"store": 1,
# 	"address": 5
# },
