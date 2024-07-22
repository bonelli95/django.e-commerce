from django.urls import path
from pystore.views import index, categories, brand, product, category_product_list, chosen_category

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('brand/', brand, name='brand'),
    path('product/', product, name='product'),
    path('category-product-list/<int:id>', category_product_list, name='category_product_list'),
    path('chosen-category/', chosen_category, name='chosen-category'),
]
