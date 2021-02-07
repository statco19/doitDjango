from django.urls import path
from . import views

urlpatterns = [
    path('/<int:pk>/', views.single_post_page),  # Page not found(404) error
    path('', views.index),
]
