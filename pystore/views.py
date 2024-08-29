from django.shortcuts import render, redirect
from pystore.models import Banner, Category, Color, Size, Product, ProductAttribute, Bag, ItemBag

def index(request):
    data = Product.objects.filter(is_featured_product = True).order_by('-id')
    return render(request, 'pystore/index.html', {'data': data})

def categories(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'pystore/category_product_list.html', {'data': data})

def product(request):
    data = Product.objects.all().order_by('-id')
    dataAtt = data.prefetch_related('productattribute_set')

    category = Product.objects.distinct().values('category__title', 'category__id')
    brands = Product.objects.distinct().values('brand__title', 'brand__id')
    color = Product.objects.distinct().values('color__title', 'color__id', 'color__color_code')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')

    return render(request, 'pystore/product.html',
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
   return render(request, 'pystore/category_product_list.html', {'data': data})

def bag(request, product_id):
    product = Product.objects.get(id=product_id)

    quantity = int(request.POST.get('quantity', 1))

    if quantity <= 0:
        return redirect('bag', product.id) 

    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag']= bag
    return redirect('bag')