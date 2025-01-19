from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("produit/", views.produit, name="produit"),
    path("contact/", views.contact, name="contact"),
    path("articles_par_cat/<int:categorie_id>/", views.Articles_par_cat, name="articles_par_cat"), # URL pattern pour afficher les articles par catégorie
]
