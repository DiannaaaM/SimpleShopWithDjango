from django.db import models
from datetime import datetime


# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=100, verbose_name="Name", help_text="Category Name")
    description = models.TextField(verbose_name="Description", help_text="Description")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __init__(self, name, description):
        self.name = name
        self.description = description

        def __str__(self):
            return f'{self.name}'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name", help_text="Product Name")
    price = models.FloatField(verbose_name="Price", help_text="Price")
    description = models.TextField(verbose_name="Description", help_text="Description")
    category = models.ForeignKey(Category, verbose_name="Category", help_text="Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', verbose_name="Image", null=True, blank=True, help_text="Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Added", help_text="Date Added", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Last Modified", help_text="Date Last Modified", null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __init__(self, name, price, description, category, image, created_at, updated_at):
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.image = image
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f'{self.category} === {self.name} -  {str(self.price)}\n {self.description}  \nYour path to image: {self.image} \n{self.created_at} \n{self.updated_at}'
