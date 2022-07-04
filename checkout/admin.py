""" Checkout admin file """

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """ line item admin class """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ order admin class """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'county',
                       'country', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'user_profile',
              'date', 'full_name',
              'email', 'phone_number', 'county',
              'postcode', 'street_address1', 'eircode',
              'street_address2', 'delivery_date',
              'timeslot', 'delivery_cost',
              'order_total', 'grand_total',
              'original_cart', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
