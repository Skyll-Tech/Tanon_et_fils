from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Dashboard.models import Article, Categorie

# Create your views here.

def home(request):
    article = Article.objects.all()
    categories = Categorie.objects.all()
    context = {'article':article, 'categories':categories}
    return render(request,"home/index.html", context)

def contact(request):
    return render(request, "home/contact.html")

def produit(request):
    return render(request, "home/produit.html")


def Articles_par_cat(request, categorie_id):  # Définition de la vue avec le paramètre categorie_id
    categorie = get_object_or_404(Categorie, id=categorie_id)  # Récupération de la catégorie ou renvoi d'une erreur 404
    articles = Article.objects.filter(Categorie_atc=categorie)  # Filtrage des articles pour cette catégorie spécifique
    categories = Categorie.objects.all()
    context = {
        'articles': articles,  # Ajout des articles filtrés au contexte
        'categorie': categorie,  # Ajout de la catégorie au contexte
        'categories': categories
    }
    return render(request, 'home/articles_par_cat.html', context)  # Rendu du template avec le contexte