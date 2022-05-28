from django.contrib import admin
from .models import Product, ProductCategory, Orders


# adjusting the view of admin dashboard
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_rented', 'user', 'days', 'rent']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price', 'color', 'product_category']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Orders,OrderAdmin)
admin.site.register(ProductCategory)


