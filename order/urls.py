from django.urls import path
from . import views

app_name='order'

urlpatterns = [
	path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
	# path('history/', views.orderHistory, name='order_history'),
	# path('<int:order_id>/', views.viewOrder, name='order_detail'),
]