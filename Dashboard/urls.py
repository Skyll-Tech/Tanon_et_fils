from django.contrib import admin
from django.urls import path
from Dashboard import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("dashboard", views.dashboard, name = "dashboard"),
    path("creer_categorie/", views.Creer_categorie, name="creer_categorie"),
    path("creer_article/", views.Creer_article, name="creer_article"),
    path("affiche_categorie/", views.affiche_categorie, name="affiche_categorie"),
    path('categories/modifier/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),

]
