from django.contrib import admin
from .models import Product, ProductCategory, Orders



class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product_rented', 'days' ,'rent')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','product_name', 'product_price' ,'product_category')


# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(Orders, OrdersAdmin)


