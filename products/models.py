""" Products app models """

from django.db import models
from django.db.models import Avg, Count
from django.core.validators import MaxValueValidator, MinValueValidator
from profiles.models import UserProfile


class Category(models.Model):
    """ Category model """

    class Meta:
        """ Meta class """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        """ Returns category friendly name"""
        return self.friendly_name


class Product(models.Model):
    """ Main product model """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def average_rating(self):
        """ calculates average product rating """
        ratings = self.rating_set.all().values_list('rating')
        avg_rating = ratings.aggregate(avg=Avg('rating')).get('avg')
        print(avg_rating)
        return avg_rating

    def count_rating(self):
        """ counts reviews """
        ratings = Rating.objects.filter(
            product=self).aggregate(count=Count('id'))
        cnt = 0
        if ratings["count"] is not None:
            cnt = int(ratings["count"])
        return cnt

    def __str__(self):
        return str(self.name)


class Rating(models.Model):
    """ product rating model """
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='ratings')
    product = models.ManyToManyField(Product)
    rating = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def get_product(self):
        return ",".join([str(p) for p in self.product.all()])

    def __str__(self):
        return str(self.rating)


class Review(models.Model):
    """ product review model """
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='reviews')
    product = models.ManyToManyField(Product)
    heading = models.CharField(max_length=100, null=True, blank=True)
    comment = models.TextField(max_length=250, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.heading)
