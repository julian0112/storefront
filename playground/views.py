from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, Func, Count, Max, Min, Avg, Sum, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db import transaction, connection
from django.contrib.contenttypes.models import ContentType
from store.models import OrderItem, Product, Order, Customer, Collection
from tags.models import TaggedItem

def say_hello(request):
    
    
    return render(request, 'hello.html', {'name': 'Julian'})