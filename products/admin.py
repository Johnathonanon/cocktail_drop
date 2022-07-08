""" Products app admin """
from django.contrib import admin
from .models import Product, Category, Rating, Review


class ProductAdmin(admin.ModelAdmin):
    """ Product admin class """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'average_rating'
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
        'rating',
        'get_product',
    )


class ReviewAdmin(admin.ModelAdmin):
    """ review admin class """
    list_display = (
        'heading',
        'comment',
        'get_product',
        'created_on',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Review, ReviewAdmin)
