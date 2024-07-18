from django.db import models
from django.utils.html import mark_safe

class Banner(models.Model):
    img = models.ImageField(upload_to="banner_img/")
    alt_text = models.CharField(max_length=250)

    def __str__(self):
        return self.alt_text
    
class Category(models.Model):
    title = models.CharField(max_length=150, null=False, blank=True, default="")
    image = models.ImageField(upload_to='cat_photos/', blank=True)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=100, null=False, blank=True, default="")
    image = models.ImageField(upload_to='brand_photos/', blank=True)

    def __str__(self):
        return self.title

class Color(models.Model):
    title = models.CharField(max_length=50)
    color_code = models.CharField(max_length=50)

    def color_tag_path(self):
        return mark_safe(self.color_code)
        
    def __str__(self):
        return self.title

class Size(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='product_photos/', blank=True)
    slug = models.CharField(max_length=250)
    detail = models.TextField()
    specification = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    is_featured_product = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product.title
    