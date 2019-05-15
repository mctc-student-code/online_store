from django.shortcuts import render, get_object_or_404
from .models import Order


def order_confirmation(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render(request,'order_confirmation.html',{'customer_order':customer_order})
