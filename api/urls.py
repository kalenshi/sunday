from django.urls import path
from rest_framework.authtoken import views

from api.customers.detail_view import CustomerDetailView
from api.customers.list_view import CustomersListView
from api.payment.list_view import PaymentList

app_name = 'api'
urlpatterns = [
	path('payments/', PaymentList.as_view(), name='payment-list'),
	path('customers/', CustomersListView.as_view(), name='customer-list'),
	path('customers/<int:customer_id>/', CustomerDetailView.as_view(), name='customer-details'),
	path('token/', views.obtain_auth_token, name='token_obtain_pair'),

]
