""" blog app views file """

from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post


def all_posts(request):
    """ view showing all blog posts """

    posts = Post.objects.filter(status=1).order_by('-created_on')
    query = None

    context = {
        'posts': posts,
        'search_term': query,
    }

    return render(request, 'blog/blogposts.html', context)


def post_details(request, post_id):
    """ View showing individual post details """

    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_details.html', context)
