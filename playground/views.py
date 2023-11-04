from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    query_set = Product.objects.all()
    query_set.filter().filter().order_by()
    
        
    return render(request, 'hello.html', {'name': 'Julian'})