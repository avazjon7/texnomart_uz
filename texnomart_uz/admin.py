from django.contrib import admin
from .models import (
    Category, Product, Image, Order, Comment,
    AttributeKey, AttributeValue, ProductAttribute
)


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category', 'created_at', 'updated_at')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'category__title')
    filter_horizontal = ('users_like',)


@admin.register(Image)
class ImageAdmin(BaseModelAdmin):
    list_display = ('product', 'is_primary', 'created_at', 'updated_at')
    list_filter = ('product', 'is_primary')
    search_fields = ('product__name',)


@admin.register(Order)
class OrderAdmin(BaseModelAdmin):
    list_display = ('user', 'product', 'quantity', 'first_payment', 'month', 'monthly_payment', 'created_at')
    list_filter = ('user', 'product',)
    search_fields = ('user__username', 'product__name')


@admin.register(Comment)
class CommentAdmin(BaseModelAdmin):
    list_display = ('user', 'product', 'rating', 'created_at')
    list_filter = ('rating', 'product')
    search_fields = ('user__username', 'product__name')


@admin.register(AttributeKey)
class AttributeKeyAdmin(admin.ModelAdmin):
    list_display = ('key_name',)
    search_fields = ('key_name',)


@admin.register(AttributeValue)
class AttributeValueAdmin(BaseModelAdmin):
    list_display = ('key_value',)
    search_fields = ('key_value',)


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'attr_key', 'attr_value')
    list_filter = ('product', 'attr_key')
    search_fields = ('product__name', 'attr_key__key_name', 'attr_value__key_value')
