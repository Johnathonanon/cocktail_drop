""" Products urls file """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product, name='delete_product'),
    path('rate/<int:product_id>/', views.rate_product, name='rate_product'),
    path('review/<int:product_id>/',
         views.review_product, name='review_product'),
]
