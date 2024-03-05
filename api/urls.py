from django.urls import path

from api.payment.list_view import PaymentList

app_name = 'api'
urlpatterns = [
	path('payments/', PaymentList.as_view(), name='payment-list'),
]
