from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.customers.serializers import CustomerSerializer
from api.models import Customer
from api.permissions import IsAdminOrReadOnly
from api.utils.pagination import CustomerPaginator


class CustomersListView(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
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
			), openapi.Parameter(
				name="email",
				description="Customer Email to filter on",
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

		filters = {}
		req_params = request.query_params
		if req_params:
			try:
				filters["first_name__icontains"] = request.query_params.get("first_name")
				filters["last_name__icontains"] = request.query_params.get("last_name")
				filters["active"] = request.query_params.get("active")
				filters["email__icontains"] = request.query_params.get(
					"email")  # TODO fix email validation

				if filters["active"] is not None:
					filters["active"] = bool(int(filters.get("active")))
				filters = {
					key: value for key, value in filters.items() if value is not None
				}
			except ValueError as e:
				return Response(
					{"error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST
				)
		if filters:

			queryset = Customer.objects.filter(**filters).order_by("customer_id")
		else:
			queryset = Customer.objects.filter(active=True).order_by("customer_id")

		result = paginator.paginate_queryset(queryset, request)
		serializer = self.serializer_class(result, many=True)

		return paginator.get_paginated_response(serializer.data)

	@swagger_auto_schema(
		request_body=CustomerSerializer,
	)
	def post(self, request, format=None):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
