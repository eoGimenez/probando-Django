from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")


class ProductAdmin(admin.ModelAdmin):
    exclude = ('created', )
    list_display = ("id", "name", "stock", "ranking", "category", "created")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
