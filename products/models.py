from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="category")

class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    product_description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")

class ProductImage(BaseModel):
    product = models.ForeignKey(Products,on_delete=models.CASCADE,related_name="product_images")
    image = models.ImageField(upload_to="product")




# Create your models here.
