"""
URL configuration for django_proj1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views


urlpatterns = [
    path("", views.loginuser, name='home'),
    path("home/", views.index, name='home'),
    path("login/", views.loginuser, name='login'),
    path("logout/", views.logoutuser, name='logout'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("user_products/", views.user_products, name='user_products'),
    path("checkout/", views.user_checkout, name='checkout'),
    path("details/<int:product_id>/", views.details, name='details'),
    path("cart/", views.cart, name='cart'),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name='add_to_cart'),
    path("clear-cart/", views.clear_cart, name='clear_cart')
    #path("remove_from_cart/", views.remove_from_cart, name='remove_from_cart'),
    #path("update_cart/", views.update_cart, name='update_cart')
]
