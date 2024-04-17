import json
from datetime import datetime

from django.core.cache import cache
from django.core.serializers.json import DjangoJSONEncoder
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema

from api.models import Payment

from api.payment.serializer import PaymentSerializer
from api.utils.pagination import PaymentPaginator


class PaymentListView(APIView):
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	serializer_class = PaymentSerializer
	pagination_class = PaymentPaginator

	@swagger_auto_schema(
		manual_parameters=[
			openapi.Parameter(
				name="payment_id",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_INTEGER,
				description="Unique Payment ID",
				required=False
			),
			openapi.Parameter(
				name="customer_id",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_INTEGER,
				description="Unique Customer ID",
				required=False
			),
			openapi.Parameter(
				name="staff_id",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_INTEGER,
				description="Unique Cashiers ID",
				required=False
			),
			openapi.Parameter(
				name="payment_date",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_STRING,
				format=openapi.FORMAT_DATETIME,
				description="Date of the order (YYYY-MM-DD)",
				required=False
			),
			openapi.Parameter(
				name="amount",
				in_=openapi.IN_QUERY,
				type=openapi.TYPE_NUMBER,
				description="Amount of the order",
				required=False
			),

		],
		responses={200: PaymentSerializer(many=True)}
	)
	def get(self, request):
		filters = {}
		req_params = request.query_params
		if req_params:
			try:
				filters["payment_id__exact"] = request.query_params.get("payment_id", )
				filters["customer_id__exact"] = request.query_params.get("customer_id", )
				filters["staff_id__exact"] = request.query_params.get("staff_id", )
				filters["amount__gte"] = request.query_params.get("amount", )
				if "payment_date" in req_params and req_params["payment_date"] is not None:
					filters["payment_date__date__exact"] = datetime.strptime(
						req_params["payment_date"], "%Y-%m-%d"
					)
				filters = {
					key: value for key, value in filters.items() if value is not None
				}
			except ValueError as e:
				return Response(
					{"error": f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST
				)
		paginator = self.pagination_class()
		if filters:
			payments = Payment.objects.select_related(
				"customer", "staff", "rental"
			).filter(**filters).order_by("payment_id")
		else:
			payments = Payment.objects.select_related(
				"customer", "staff", "rental"
			).all().order_by("payment_id")
		# At this point the query has not yet hit the database

		query_string = f"payment:{json.dumps(filters, indent=4, sort_keys=True, cls=DjangoJSONEncoder)}"

		# check the cache
		if cache.get(query_string):
			result = paginator.paginate_queryset(cache.get(query_string, ), request)
		else:
			result = paginator.paginate_queryset(payments, request)
			cache.set(query_string, result, timeout=5 * 60)
		serializer = self.serializer_class(result, many=True)
		return paginator.get_paginated_response(serializer.data)
