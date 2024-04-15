from django.contrib import admin
from .models import Product, Category, Material, Color, Gender, Size, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category')


admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(Gender)
admin.site.register(Size)
admin.site.register(Brand)
