from django.urls import path

from api.customers.detail_view import CustomerDetailView
from api.customers.list_view import CustomersListView
from api.payment.list_view import PaymentListView

app_name = 'api'
urlpatterns = [
	path('payments/', PaymentListView.as_view(), name="payment-list"),
	path('customers/', CustomersListView.as_view(), name="customers-list"),
	path('customers/<int:customer_id>/', CustomerDetailView.as_view(), name="customer-details"),
]
