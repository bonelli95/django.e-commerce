from django.contrib import admin
from pystore.models import Category, Brand, Size, Color, Product, ProductAttribute

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Color)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'color', 'size', 'status')
    list_editable = ('status',)

admin.site.register(Product, ProductAdmin)

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size')

admin.site.register(ProductAttribute, ProductAttributeAdmin)