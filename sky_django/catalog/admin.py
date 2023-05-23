from django.contrib import admin

from catalog.models import Product, Category, Contact


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

