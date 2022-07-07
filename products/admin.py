""" Products app admin """
from django.contrib import admin
from .models import Product, Category, Rating


class ProductAdmin(admin.ModelAdmin):
    """ Product admin class """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """ Category admin class """
    list_display = (
        'friendly_name',
        'name',
    )


class RatingAdmin(admin.ModelAdmin):
    """ Rating admin class """
    list_display = (
        'product',
        'rating',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
