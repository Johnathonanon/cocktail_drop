""" Cart views file """
from django.shortcuts import render


def view_cart(request):
    """ View showing the cart contents page """

    return render(request, 'cart/cart.html')
