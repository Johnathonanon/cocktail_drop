""" products app forms file """
from django import forms
from .models import Product, Category, Rating, Review


class ProductForm(forms.ModelForm):
    """ product form class """
    class Meta:
        """ meta class """
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-form-input'


class RatingForm(forms.ModelForm):
    """ product review form class """
    class Meta:
        """ meta class """
        model = Rating
        exclude = ('user_profile',)
        fields = (
            'rating',
        )

    def __init__(self, *args, **kwargs):
        """
        custom init method
        """
        super().__init__(*args, **kwargs)

        self.fields['rating'].widget.attrs['min'] = 1
        self.fields['rating'].widget.attrs['max'] = 5


class ReviewForm(forms.ModelForm):
    """ product review form class """
    class Meta:
        """ meta class """
        model = Review
        exclude = ('user_profile',)
        fields = (
            'heading',
            'comment',
        )
