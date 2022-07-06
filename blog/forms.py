""" blog app forms file """
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """ post form class """
    class Meta:
        """ meta class """
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'blog-form-input'
