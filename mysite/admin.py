from django.contrib import admin
from .models import Product, Category, Material, Color, Gender, Size, Brand, News, FeaturedProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_recommend')
    list_filter = ['is_recommend']
    search_fields = ('name', 'category')


@admin.register(News)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')


@admin.register(FeaturedProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'release_date')


admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Color)
admin.site.register(Gender)
admin.site.register(Size)
admin.site.register(Brand)
