""" profiles app forms file """

from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ form allowing user to set delivery data """
    class Meta:
        """ meta class """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postcode',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'Co. Dublin',
            'default_eircode': 'Eircode',
            'default_country': 'Country',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        self.fields['default_county'].disabled = True
        self.fields['default_country'].disabled = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            self.fields[field].label = False
