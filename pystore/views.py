from django.shortcuts import render
from pystore.models import Banner, Category, Brand, Color, Size, Product, ProductAttribute

def index(request):
    return render(request, 'index.html')

def categories(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'categories.html', {'data':data})

def brand(request):
    data = Brand.objects.all().order_by('-id')
    return render(request, 'brand.html', {'data': data})

def product(request):
    data = Product.objects.all().order_by('-id')
    return render(request, 'product.html', {'data': data})