from django.contrib import admin
from .models import Product, ProductCategory, Orders

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Orders)


