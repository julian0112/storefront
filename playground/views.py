from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import OrderItem, Product, Order

def say_hello(request):
    # quearyset = Product.objects.prefetch_related('promotions').select_related('collection').all()
    quearyset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
        
    return render(request, 'hello.html', {'name': 'Julian', 'orders': list(quearyset)})