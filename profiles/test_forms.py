""" profile app forms test file """
from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """ Profile form test class """

    def test_fields_required(self):
        """ test required form fields """
        form = UserProfileForm({
            'default_postcode': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('default_postcode', form.errors.keys())
        self.assertEqual(
            form.errors['default_postcode'][0], 'This field is required.')

    def test_fields_not_required(self):
        """ test not required form fields """
        form = UserProfileForm({
            'default_postcode': 'Dublin 1',
        })
        self.assertTrue(form.is_valid())

    def test_fields_in_metaclass(self):
        """ test correct meta fields"""
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))
