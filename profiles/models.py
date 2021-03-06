""" profiles app models file """
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """

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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=10, choices=POSTCODE_CHOICES, default='')
    default_county = models.CharField(
        max_length=80, null=True, blank=True, default='Co. Dublin')
    default_eircode = models.CharField(
        max_length=7, null=True, blank=True, default='')
    default_country = models.CharField(
        max_length=10, default='IE', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
