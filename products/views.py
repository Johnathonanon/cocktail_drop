""" Products views file """

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from profiles.models import UserProfile
from .models import Product, Category, Rating, Review
from .forms import ProductForm, RatingForm, ReviewForm


def all_products(request):
    """ View showing all products, including sorting and search queries """

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    products = list(set(list(products)))

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ View showing individual product details """

    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.\
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def rate_product(request, product_id):
    """ allows user to rate product """

    product = Product.objects.get(pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    user_rating = Rating.objects.filter(product=product, user_profile=profile)

    if user_rating:
        messages.error(request, 'You have already rated this product.\
            Why not rate a different product?')
        return redirect(reverse('product_details', args=[product.id]))

    if request.method == 'POST':

        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user_profile = profile
            rating.save()
            rating.product.add(product)
            messages.success(request, 'Thanks for leaving a rating!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to leave rating.\
                Please ensure the form is valid.')
    else:
        form = RatingForm(instance=product)
        messages.info(request, f'You are rating {product.name}')

    template = 'products/rate_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def review_product(request, product_id):
    """ allows user to review product """

    product = Product.objects.get(pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    user_review = Review.objects.filter(product=product, user_profile=profile)

    if user_review:
        messages.error(request, 'You have already reviewed this product.\
            Please feel free to review another of our delicious creations!')
        return redirect(reverse('product_details', args=[product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user_profile = profile
            review.save()
            review.product.add(product)
            messages.success(request, 'Thanks for leaving a review!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to leave review.\
                Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=product)
        messages.info(request, f'You are reviewing {product.name}')

    template = 'products/review_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
