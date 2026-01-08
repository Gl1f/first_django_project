from django.shortcuts import render
from django.http import Http404
from .data import masters, orders

all_orders = []
for order in orders:
    master_name = next((master['name'] for master in masters if master['id'] == order['master_id']), 'Неизвестный мастер')
    order_info = order.copy()
    order_info['master_name'] = master_name
    all_orders.append(order_info)

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def thanks(request):
    context = {'title': 'Спасибо за вашу заявку!', 'message': 'Мы свяжемся с вами в ближайшее время.'}
    return render(request, 'core/thanks.html', context)

def orders_list(request):
    context = {'orders': all_orders}
    return render(request, 'core/orders_list.html', context)

def order_detail(request, order_id):
    order = next((order for order in all_orders if order['id'] == order_id), None)
    if order is None:
        raise Http404("Заявка не найдена")
    context = {'order': order}
    return render(request, 'core/order_detail.html', context)