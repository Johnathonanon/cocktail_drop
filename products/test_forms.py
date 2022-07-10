""" product app forms test file """
from django.test import TestCase
from .forms import ProductForm, RatingForm, ReviewForm
from .models import Product


class TestProductForm(TestCase):
    """ Product form test class """

    def test_fields_required(self):
        """ test required form fields """
        form = ProductForm({
            'name': '',
            'description': '',
            'price': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('description', form.errors.keys())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_fields_not_required(self):
        """ test not required form fields """
        form = ProductForm({
            'name': 'name',
            'description': 'description',
            'price': 5,
        })
        self.assertTrue(form.is_valid())

    def test_fields_in_metaclass(self):
        """ test correct meta fields"""
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')


class TestRatingForm(TestCase):
    """ rating form test class """

    def test_fields_required(self):
        """ test required form fields """
        form = RatingForm({
            'rating': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('rating', form.errors.keys())
        self.assertEqual(form.errors['rating'][0], 'This field is required.')

    def test_fields_not_required(self):
        """ test not required form fields """
        form = RatingForm({
            'product': Product(),
            'rating': 5,
        })
        self.assertTrue(form.is_valid())

    def test_fields_in_metaclass(self):
        """ test correct meta fields """
        form = RatingForm()
        self.assertEqual(form.Meta.fields, ('rating',))


class TestReviewForm(TestCase):
    """ review form test class """

    def test_fields_required(self):
        """ test required fields """
        form = ReviewForm({
            'heading': '',
            'comment': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('heading', form.errors.keys())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['heading'][0], 'This field is required.')
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_fields_in_metaclass(self):
        """ test correct meta fields """
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, (
            'heading',
            'comment',
        ))
