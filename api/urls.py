from django.urls import path

from api.customers.list_view import CustomersList
from api.payment.list_view import PaymentList

app_name = 'api'
urlpatterns = [
	path('payments/', PaymentList.as_view(), name='payment-list'),
	path('customers/', CustomersList.as_view(), name='customer-list'),
]
