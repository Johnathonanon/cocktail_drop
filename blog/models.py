""" blog app models file """

from django.db import models
from profiles.models import UserProfile


class Post(models.Model):
    """ Blog post class """

    STATUS = ((0, "Draft"), (1, "Published"))

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField(null=True, blank=True)
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        UserProfile, related_name='blog_likes', blank=True)

    class Meta:
        """ meta class """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def number_of_likes(self):
        """ returns number of likes on post """
        self.likes.count()
