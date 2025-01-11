from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("produit/", views.produit, name="produit"),
    path("contact/", views.contact, name="contact"),
]
