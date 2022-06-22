""" Products views file """

from django.shortcuts import render
from .models import Product


def all_products(request):
    """ View showing all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
