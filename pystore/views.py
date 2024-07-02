from django.shortcuts import render
from pystore.models import Banner, Category, Brand, Color, Size, Product, ProductAttribute

def index(request):
    return render(request, 'pystore/index.html')
