from django.shortcuts import render
from db_berbershop import masters, services, orders, STATUS_NEW, STATUS_CONFIRMED, STATUS_CANCELLED, STATUS_COMPLETED
# Create your views here.
def landing(request):
    context = {'masters': masters, 'services': services}
    return render(request, 'landing.html', context)

def thanks(request):
    context = {'message': 'Спасибо за ваш заказ!',
                'status': STATUS_NEW}
    return render(request, 'thanks.html', context)

def orders_list(request):
    return render(request, 'orders/list.html')

def order_detail(request, order_id):
    return render(request, 'orders/detail.html', {'order_id': order_id})