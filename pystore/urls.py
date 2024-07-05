from django.urls import path
from pystore.views import index, categories

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories')
]
