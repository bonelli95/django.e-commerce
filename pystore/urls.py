from django.urls import path
from pystore.views import index, categories, product, category_product_list

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('product/', product, name='product'),
    path('category_product_list/<int:cat_id>', category_product_list, name='category_product_list'),

]
