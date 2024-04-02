from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from api.customers.serializers import CustomerSerializer
from api.models import Customer


class CustomerDetailView(APIView):
	# permission_classes = [IsAuthenticatedOrReadOnly]
	serializer_class = CustomerSerializer

	@staticmethod
	def get_object(pk):
		return get_object_or_404(Customer, pk=pk)

	def get(self, request, customer_id):
		customer = self.get_object(customer_id)
		serializer = self.serializer_class(instance=customer)
		return Response(serializer.data, status=status.HTTP_200_OK)

	@swagger_auto_schema(
		operation_description="Change the active status on a Customer to False "
	)
	def delete(self, request, customer_id=None):
		customer = self.get_object(customer_id)
		serializer = self.serializer_class(instance=customer)
		customer.active = False
		customer.save()
		return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

	@swagger_auto_schema(
		operation_description="Update the customers email or active status to True",
		request_body=openapi.Schema(
			type=openapi.TYPE_OBJECT,
			properties={
				"email": openapi.Schema(type=openapi.TYPE_STRING),
				"active": openapi.Schema(type=openapi.TYPE_NUMBER, enum=[0, 1])
			}
		),
		responses={
			status.HTTP_206_PARTIAL_CONTENT: CustomerSerializer(partial=True),
			status.HTTP_400_BAD_REQUEST: CustomerSerializer()
		}

	)
	def patch(self, request, customer_id=None):
		customer = self.get_object(customer_id)
		serializer = self.serializer_class(
			instance=customer, data=request.data, partial=True
		)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
