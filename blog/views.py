""" blog app views file """

from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from .models import Post


def all_posts(request):
    """ view showing all blog posts """

    BLOG = True

    posts = Post.objects.filter(status=1).order_by('-created_on')
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria")
                return redirect(reverse('blog'))

            queries = Q(title__icontains=query) | Q(
                content__icontains=query)
            posts = posts.filter(queries)

    context = {
        'posts': posts,
        'search_term': query,
    }

    return render(request, 'blog/blogposts.html', context)
