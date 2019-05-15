from django.urls import path
from . import views

app_name='order'

urlpatterns = [
	path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
]