""" Cart templatetags cart tools file """
from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """ Calculates cart subtotal """
    return price * quantity
