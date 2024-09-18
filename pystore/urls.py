from django.urls import path
from pystore.views import index, categories, product, category_product_list, bag, buy, clear_bag

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('product/', product, name='product'),
    path('category_product_list/<int:cat_id>', category_product_list, name='category_product_list'),
    path('bag/<int:product_id>/', bag, name='bag_add'),
    path('bag/', bag, name='bag'),
    path('bag/buy/', buy, name='buy'),
    path('clear_bag/', clear_bag, name='clear_bag'),
]
