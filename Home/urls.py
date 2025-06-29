from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.home, name="home"),
    path("all_article/", views.All_article, name="article"),
    path("contact/", views.contact, name="contact"),
    path("articles_par_cat/<int:categorie_id>/", views.Articles_par_cat, name="articles_par_cat"), 
    path("details_article/<int:article_id>/",views.Details_article, name="details_article"),
    path("service_page/", views.Service_page, name="service_page"),
]