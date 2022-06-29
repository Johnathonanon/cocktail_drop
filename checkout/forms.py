""" checkout forms file """
import datetime

from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """ order form class """
    class Meta:
        """ meta class """
        model = Order

        readonly_fields = ('city', 'county', 'country')

        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'postcode', 'delivery_date', 'timeslot')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'delivery_date': datetime.date.today,
            'timeslot': '1'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
