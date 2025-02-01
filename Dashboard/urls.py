from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from Dashboard import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("dashboard", views.dashboard, name = "dashboard"),
    
    path("creer_categorie/", views.Creer_categorie, name="creer_categorie"),
    path("affiche_categorie/", views.affiche_categorie, name="affiche_categorie"),
    path('categories/modifier/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
    
    path("creer_article/", views.Creer_article, name="creer_article"),
    path("afficher_article/", views.Afficher_article, name="afficher_article"),
    path("supprimer_article/supprimer/<int:id>/", views.Supprimer_article, name="supprimer_article"),

    path("creer_service/", views.Creer_service, name="creer_service"),
    path("afficher_services/", views.Afficher_services, name="afficher_services"),
    path("supprimer_service/supprimer/<int:id>/", views.Supprimer_service, name="supprimer_service"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
