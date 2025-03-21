from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from pystore.models import Banner, Category, Color, Size, Product, ProductAttribute, Bag, ItemBag
from django.contrib import messages
from django.conf import settings
from django.views import View
from django.http import HttpRequest, JsonResponse
from django.views.generic import TemplateView
import stripe
from django.contrib.auth.decorators import login_required

stripe.api_key = settings.STRIPE_SECRET_KEY

def index(request):
    data = Product.objects.filter(is_featured_product = True).order_by('-id')
    return render(request, 'pystore/index.html', {'data': data})

def categories(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'pystore/categories.html', {'data': data})

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
    if not request.user.is_authenticated:
        messages.error(request, 'Please log in to access this page.')
        return redirect('login')
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
                    'image_url': product.image.url
                })
            else:
                print(f"Erro: item_data to attribute_id {attribute_id} it's not a dictionary.")

        total_price = sum(item['total_price'] for item in bag_items)

        context = {
            'bag_items': bag_items,
            'total_price': total_price,
        }

        return render(request, 'store/bag.html', context)

class ProductLandingPageView(TemplateView):
    template_name = 'store/landing.html'

    def get_context_data(self, **kwargs ):
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        
        bag = self.request.session.get('bag', {})
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
                    'image_url': product.image.url
                })
        
        total_price = sum(item['total_price'] for item in bag_items)

        context.update({
            'total_price': total_price,
            'bag_items': bag_items,
            'product': product,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
        })
        return context
          
    
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        bag = self.request.session.get('bag', {})

        YOUR_DOMAIN = settings.YOUR_DOMAIN
        line_items = []

        for attribute_id, item_data in bag.items():
            product = get_object_or_404(Product, id=item_data['product_id'])
            product_attribute = get_object_or_404(ProductAttribute, id=attribute_id)
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(product_attribute.price * 100),
                    'product_data': {
                        'name': product.title,
                    },
                },
                'quantity': item_data['quantity'],
            })

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + 'success/',
            cancel_url=YOUR_DOMAIN + 'cancel/',
        )
        
        return JsonResponse({
            'id': checkout_session.id
        })

@login_required
def success(request):
    name_user = request.user.username
    email_user = request.user.email
    context = {'name_user': name_user, 'email_user': email_user}
    return render(request, 'store/success.html', context)

@login_required   
def cancel(request):
    name_user = request.user.username
    context = {'name_user': name_user}
    return render(request, 'store/cancel.html', context)
    
def clear_bag(request):
    request.session['bag'] = {}
    return redirect('bag')
