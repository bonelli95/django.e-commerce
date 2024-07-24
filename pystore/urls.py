from django.urls import path
from pystore.views import index, categories, brand, product, chosen_category

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    path('brand/', brand, name='brand'),
    path('product/', product, name='product'),
    path('chosen-category/<int:id>', chosen_category, name='chosen-category'),
]
