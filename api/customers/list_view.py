from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.customers.serializers import CustomerSerializer
from api.models import Customer
from api.permissions import IsAdminOrReadOnly
from api.utils.pagination import CustomerPaginator


class CustomersList(APIView):
	permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]
	serializer_class = CustomerSerializer
	pagination_class = CustomerPaginator

	@swagger_auto_schema(
		manual_parameters=[
			openapi.Parameter(
				name="first_name",
				description="Customer First Name to filter on",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_STRING,
				required=False
			),
			openapi.Parameter(
				name="last_name",
				description="Customer Last Name to filter on",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_STRING,
				required=False
			),
			openapi.Parameter(
				name="active",
				description="Customer Still Using our System",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_INTEGER,
				required=False
			),
		],
		responses={"200": CustomerSerializer, "400": openapi.Response("CustomerSerializer.errors")}
	)
	def get(self, request, format=None):
		paginator = self.pagination_class()
		queryset = Customer.objects.all()

		result = paginator.paginate_queryset(queryset, request)
		serializer = self.serializer_class(result, many=True)

		return paginator.get_paginated_response(serializer.data)

	@swagger_auto_schema(
		request_body=CustomerSerializer,


	)
	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
