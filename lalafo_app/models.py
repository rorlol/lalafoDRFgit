from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30,unique=True)
    category_image = models.ImageField(upload_to='category_image/')

    def __str__(self):
        return self.category_name

class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = PhoneNumberField()
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    product_image = models.ImageField(upload_to='images',null=True,blank=True)

    def __str__(self):
        return self.product_name