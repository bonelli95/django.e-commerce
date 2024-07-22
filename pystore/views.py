from django.shortcuts import render
from pystore.models import Banner, Category, Brand, Color, Size, Product, ProductAttribute, ChosenCategory

def index(request):
    data = Product.objects.filter(is_featured_product = True).order_by('-id')
    return render(request, 'index.html', {'data': data})

def categories(request):
    categories_type = ChosenCategory.CATEGORY_CHOICES
    data = Category.objects.all().order_by('-id')
    context = {'categories_type': categories_type, 'data': data}
    return render(request, 'categories.html', context)

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
  category = Category.objects.get(id=cat_id)
  data = Product.objects.filter(category=category).order_by('-id')
  return render(request, 'category_product_list.html', {'data': data})

def chosen_category(request):
    category_type = request.GET.get('type')
    if category_type:
        categories = ChosenCategory.objects.filter(category_type=category_type)
    else:
        categories = ChosenCategory.objects.all()
    return render(request, 'chosen_category.hmtl', {'category' : categories})