from django.urls import path
from pystore.views import index

urlpatterns = [
    path('', index, name='index'),
]
