from django.shortcuts import get_object_or_404, render, redirect
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

def bag(request, product_id=None):
    bag = request.session.get('bag', {})
    if product_id is not None:
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        if quantity <= 0:
            return redirect('bag_add', product_id=product_id)
        
        product_attribute = ProductAttribute.objects.filter(product=product).first()
        if not product_attribute:
            return redirect('bag')

        #bag = request.session.get('bag', {})

        attribute_id = str(product_attribute.id)
        if attribute_id in bag:
            if isinstance(bag[attribute_id], dict):
                bag[attribute_id]['quantity'] += quantity
            else:
                existing_quantity = bag[attribute_id] if isinstance(bag[attribute_id], int) else 0
                bag[attribute_id] = {
                    'product_id': product.id,
                    'quantity': existing_quantity + quantity,
                    'price': float(product_attribute.price),
                }
        else:
            bag[attribute_id] = {
                'product_id': product.id,
                'quantity': quantity,
                'price': float(product_attribute.price),
            }

        request.session['bag'] = bag
        return redirect('bag')
    else:
        bag = request.session.get('bag', {})
        bag_items = []

        for attribute_id, item_data in bag.items():
            if isinstance(item_data, dict):
                product = get_object_or_404(Product, id=item_data['product_id'])
                product_attribute = get_object_or_404(ProductAttribute, id=attribute_id)
                bag_items.append({
                    'product': product,
                    'quantity': item_data['quantity'],
                    'price': item_data['price'],
                    'total_price': item_data['price'] * item_data['quantity'],
                })
            else:
                print(f"Erro: item_data para attribute_id {attribute_id} não é um dicionário.")

        total_price = sum(item['total_price'] for item in bag_items)

        context = {
            'bag_items': bag_items,
            'total_price': total_price,
        }

        return render(request, 'pystore/bag.html', context)
    
def clear_bag(request):
    request.session['bag'] = {}
    return redirect('bag')