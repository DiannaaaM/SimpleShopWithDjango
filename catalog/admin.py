from django.contrib import admin
from catalog.models import Products, Category

# Register your models here.
@admin.register('products')
class productAdmin(admin.Admin):
    list_display = ('name', 'price', 'description', 'created_at', 'updated_at')

@admin.register('category')
class categoryAdmin(admin.Admin):
    list_display = ('name', 'description')