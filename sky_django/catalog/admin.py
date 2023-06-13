from django.contrib import admin

from catalog.models import Product, Category, Contact, Post, Version


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'title', 'category')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'slug', 'preview', 'created_at', 'is_published', 'count_views')


@admin.register(Version)
class PostAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name_version', 'is_active')
