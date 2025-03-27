from django.contrib import admin
from catalog.models import Products, Category

# Register your models here.
@admin.register('products')
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'image', 'created_at', 'updated_at')

    class Meta:
        verbose_name_plural = 'products'

@admin.register('category')
class categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

    class Meta:
        verbose_name_plural = 'categories'