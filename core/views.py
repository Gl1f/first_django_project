from django.shortcuts import render
from core.db_barbershop import masters, services, orders, STATUS_NEW
from django.http import Http404
# Create your views here.
def landing(request):
    context = {'masters': masters, 'services': services}
    return render(request, 'landing.html', context)

def thanks(request):
    context = {'message': 'Спасибо за ваш заказ!',
                'status': STATUS_NEW}
    return render(request, 'thanks.html', context)

def orders_list(request):
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id: int):
    order = next((o for o in orders if o["id"] == order_id), None)
    if order is None:
        raise Http404(f"Заказ id={order_id} не найден")
    return render(request, "orders/order_detail.html", {"order": order})