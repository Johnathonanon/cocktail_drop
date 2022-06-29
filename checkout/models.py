""" Checkout models file """
import uuid
import datetime

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class DeliverySlot(models.Model):
    """ Delivery slot model """

    class Meta:
        """ Meta class """
        unique_together = ('date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '10:00 - 11:00'),
        (1, '11:00 - 12:00'),
        (2, '12:00 - 13:00'),
        (3, '13:00 - 14:00'),
        (4, '14:00 - 15:00'),
        (5, '15:00 - 16:00'),
        (6, '16:00 - 17:00'),
        (7, '17:00 - 18:00'),
        (8, '18:00 - 19:00'),
        (9, '19:00 - 20:00'),
        (10, '20:00 - 21:00'),
    )

    date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)

    def __str__(self):
        return f'{self.timeslot}'


class Order(models.Model):
    """ Order model """

    D1 = 'Dublin 1'
    D2 = 'Dublin 2'
    D4 = 'Dublin 4'
    D6 = 'Dublin 6'
    D7 = 'Dublin 7'
    D8 = 'Dublin 8'
    D12 = 'Dublin 12'

    POSTCODE_CHOICES = [
        (D1, 'Dublin 1'),
        (D2, 'Dublin 2'),
        (D4, 'Dublin 4'),
        (D6, 'Dublin 6'),
        (D7, 'Dublin 7'),
        (D8, 'Dublin 8'),
        (D12, 'Dublin 12'),
    ]

    TIMESLOT_CHOICES = [
        (0, '10:00 - 11:00'),
        (1, '11:00 - 12:00'),
        (2, '12:00 - 13:00'),
        (3, '13:00 - 14:00'),
        (4, '14:00 - 15:00'),
        (5, '15:00 - 16:00'),
        (6, '16:00 - 17:00'),
        (7, '17:00 - 18:00'),
        (8, '18:00 - 19:00'),
        (9, '19:00 - 20:00'),
        (10, '20:00 - 21:00'),
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(
        max_length=10, choices=POSTCODE_CHOICES, default=D2)
    city = models.CharField(
        max_length=6, null=False, default='Dublin', editable=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(
        max_length=6, null=False, default='Dublin', editable=False)
    delivery_date = models.DateField(help_text="DD-MM-YYYY",
                                     default=datetime.date.today)
    timeslot = models.IntegerField(choices=TIMESLOT_CHOICES, default=8)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """ Line item model """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
