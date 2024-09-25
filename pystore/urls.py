from django.urls import path
from pystore.views import index, categories, product, category_product_list, bag, clear_bag, CreateCheckoutSessionView, ProductLandingPageView, success, cancel

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('product/', product, name='product'),
    path('category_product_list/<int:cat_id>/', category_product_list, name='category_product_list'),
    path('bag/<int:product_id>/', bag, name='bag_add'),
    path('bag/', bag, name='bag'),
    path('clear_bag/', clear_bag, name='clear_bag'),
    path('landing/', ProductLandingPageView.as_view(), name='landing'),
    path('create-checkout-session/<int:product_id>', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', success, name='success'),
    path('cancel/', cancel, name='cancel'),
]
