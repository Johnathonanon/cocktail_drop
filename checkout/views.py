""" checkout views file """

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ renders checkout view """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KxYVNK1fke01IYS97o1sffIIXhx9633m2cImvP2vCU8Fg5L9N30WHnEJBENv3HrPRaWYHEOenIaK3L3rZWERuJ400Y2CZEdoj',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
