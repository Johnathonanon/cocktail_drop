""" blog app admin file """
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """ Post admin class """
    list_display = (
        'title',
        'status',
        'created_on',
    )

    ordering = ('-created_on',)


admin.site.register(Post, PostAdmin)
