from django.contrib import admin

from .models import CategoryModel, CartModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk','category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']
    ordering = ['category_title']

from .models import ProductModel
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'product_title', 'product_price', 'product_created_at']
    search_fields = ['product_title']
    list_filter = ['product_created_at']
    ordering = ['product_title']

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_add_date']