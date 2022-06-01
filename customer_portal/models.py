from dataclasses import fields
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

# Model for the Product
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100)
    product_category = models.ForeignKey('customer_portal.ProductCategory', on_delete=models.CASCADE, null=False, blank=False)
    featured_image = models.ImageField(upload_to='product_images',null=False, blank=False) #upload_to will go to base_dir/static/media/product_images then it will 
    date_added = models.DateTimeField(auto_now_add=True)
    product_availability = models.BooleanField(default=False)

    # displays the name the product as 'Products' in the admin dashboard
    class Meta:
        verbose_name_plural = 'Products'

    #shows what is first thing you will see in the database
    def __str__(self):
        return self.product_name

    @property #lets rendering out data by the method instead of by attribute
    def imageURL(self):
          try:
               img = self.featured_image.url # sets the 
          except:
               img = '' # sets to nothing, if the image is not found
          return img

# Model of the Order
class Orders(models.Model): 
     # Prevent deletion of the referenced object by raising ProtectedError
    user = models.ForeignKey(User, on_delete=models.PROTECT)# this will be automatically be populated in the views.py under the checkout.class
    product_rented = models.ForeignKey("customer_portal.Product",  on_delete = models.SET_NULL, blank = True, null= True) # this will be automatically be populated in the views.py

     # Setting a cap on how many days to rent the product
    days = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)]) # this will only be the field in the order form
    rent = models.CharField(max_length=8) # this will only be the field in the order form
    is_complete = models.BooleanField(default = False)
   
    # displays the name the orders as 'Pending Orders' in the admin dashboard
    class Meta:
        verbose_name_plural = 'Pending Orders'

    # displays the title of the in the row 
    def __str__(self): 
        return f"Order: {self.id}"
    
class ProductCategory(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='category_images', null=True, blank = False)     #upload_to will go to base_dir/static/media/product_images then it will go to category_images dir
    created = models.DateTimeField(auto_now_add=True)
    category_id = models.UUIDField(default= uuid.uuid4, editable=False, unique=True, primary_key=True)

    # displays the name the orders as 'Pending Orders' in the admin dashboard
    class Meta:
        verbose_name_plural = 'Product Category'

    # displays the title of the in the row 
    def  __str__(self):     
          return self.title