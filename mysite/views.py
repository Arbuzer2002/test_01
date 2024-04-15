from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import HttpResponse


def home(request):
    return render(request, 'mysite/home.html')


def shop(request):
    products = Product.objects.all()
    return render(request, 'mysite/shop.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    total_sizes = product.sizes.aggregate(total=Sum('quantity'))['total']
    total_sizes = total_sizes if total_sizes is not None else 0
    return render(request, 'mysite/product_detail.html', {'product': product, 'total_sizes': total_sizes})


def page(request):
    return render(request, 'mysite/tast.html')
