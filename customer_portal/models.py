from dataclasses import fields
from django.db import models
from django.contrib.auth.models import User
import uuid

# Model for the Product
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100)
    product_category = models.ForeignKey('customer_portal.ProductCategory', on_delete=models.CASCADE, null=False, blank=False)

    #upload_to will go to base_dir/static/media/product_images then it will 
    featured_image = models.ImageField(upload_to='product_images',null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    product_availability = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Products'

    #shows what is first thing you will see in the database
    def __str__(self):
        return self.product_name

    @property #lets rendering out data by the method instead of by attrib
    def imageURL(self):
          try:
               img = self.featured_image.url
          except:
               img = ''
          return img

# Model of the Order
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product_rented = models.ForeignKey("customer_portal.Product",  on_delete = models.SET_NULL, blank = True, null= True)
    days = models.CharField(max_length=3)
    rent = models.CharField(max_length=8)
    is_complete = models.BooleanField(default = False)
   
    class Meta:
        verbose_name_plural = 'Pending Orders'

    # displays the title of the row
    def __str__(self): 
        return f"Order: {self.id}"
    
 
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    #upload_to will go to base_dir/static/media/product_images then it will go to category_images dir
    image = models.ImageField(upload_to='category_images', null=True, blank = False)
    created = models.DateTimeField(auto_now_add=True)
    category_id = models.UUIDField(default= uuid.uuid4, editable=False, unique=True, primary_key=True)

    class Meta:
        verbose_name_plural = 'Product Category'

    def  __str__(self):     
          return self.title