from django.shortcuts import render
from pystore.models import Banner, Category, Brand, Color, Size, Product, ProductAttribute

def index(request):
    data = Product.objects.filter(is_featured_product = True).order_by('-id')
    return render(request, 'index.html', {'data': data})

def categories(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category_product_list.html', {'data': data})

def brand(request):
    data = Brand.objects.all().order_by('-id')
    return render(request, 'brand.html', {'data': data})

def product(request):
    data = Product.objects.all().order_by('-id')
    dataAtt = data.prefetch_related('productattribute_set')

    category = Product.objects.distinct().values('category__title', 'category__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    color = Product.objects.distinct().values('color__title', 'color__id', 'color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')

    return render(request, 'product.html',
    {
        'data': data,
        'category': category,
        'brands': brands,
        'color': color,
        'sizes': sizes,
        'dataAtt':dataAtt,
    })

def category_product_list(request, cat_id):
   category = Category.objects.get(pk=cat_id)
   data = Product.objects.filter(category=category).order_by('-id')
   return render(request, 'category_product_list.html', {'data': data})