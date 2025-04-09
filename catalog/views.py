from django.shortcuts import render, get_object_or_404
from catalog.models import Products, Category


# Create your views here.

def home(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def contacts(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'contacts.html', context)


def products_list(request):
    products = Products.objects.all()
    context = {"products": products}
    return render(request, 'base.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    return render(request, 'product_detail.html', {'product': product})