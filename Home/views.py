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


def Articles_par_cat(request, categorie_id):
    categorie = get_object_or_404(Categorie, id=categorie_id)  
    articles = Article.objects.filter(Categorie_atc=categorie)  
    categories = Categorie.objects.all()
    context = {
        'articles': articles, 
        'categorie': categorie,  
        'categories': categories
    }
    return render(request, 'home/articles_par_cat.html', context)  

def Details_article(request, article_id):
    article = get_object_or_404(Article, id = article_id)
    articles = Article.objects.all()
    categories = Categorie.objects.all()
    context = {'article':article, 'articles':articles, 'categories':categories}
    return render(request, 'home/details_article.html',context)