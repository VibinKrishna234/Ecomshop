from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .models import Cart



def products(request):
    product = Product.objects.all()
    return render(request, 'frontend/products.html', {'products': product})


def homepage(request):
    return HttpResponse("this is home page")



def cartlist(request):
    cartlist = Cart.objects.all()
    return render(request, 'frontend/cartlist.html', {'cartlist': cartlist})