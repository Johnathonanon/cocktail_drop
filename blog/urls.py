""" Blog urls file """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('<int:post_id>/', views.post_details, name='post_details'),
    path('create/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/',
         views.delete_post, name='delete_post'),
]
