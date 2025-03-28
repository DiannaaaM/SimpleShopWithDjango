from django.shortcuts import render
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
