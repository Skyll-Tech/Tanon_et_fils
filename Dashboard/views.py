from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages 
from django.db import IntegrityError
from .models import Categorie, Article, Services
from .forms import Articles_form, Services_form


# Create your views here.
def test(request):
    return HttpResponse("Bonjour")

def dashboard(request):
    categorie = Categorie.objects.all()
    context = {'categorie':categorie}
    return render(request, "dashboard/index.html", context)


def Creer_categorie(request):
    if request.method == 'POST':
        Nom_categorie = request.POST['Nom_categorie']
        if Nom_categorie:
            try:
                categorie = Categorie.objects.create(Nom_categorie = Nom_categorie, Nb_article = 0)
                messages.success(request,'La catégorie a été créée avec succes!')
                return redirect('creer_categorie')
            
            except IntegrityError:
                messages.error(request, 'une catégorie de ce nom existe déjà')
                
            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite: {str(e)}')
                
        else: messages.error(request, 'Le nom de la catégorie ne peut pas être vide.')
        
    return render(request,"dashboard/categories/creer_categorie.html")



def modifier_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST': 
        Nom_categorie = request.POST['Nom_categorie']  
        if Nom_categorie:  
            categorie.Nom_categorie = Nom_categorie  # Met à jour le nom de la catégorie
            try:
                categorie.save()   
                messages.success(request, 'La catégorie a été modifiée avec succès !') 
                return redirect('creer_categorie')  
            except IntegrityError:  
                messages.error(request, 'Une catégorie avec ce nom existe déjà. Veuillez choisir un autre nom.')
            except Exception as e: 
                messages.error(request, f'Une erreur s\'est produite: {str(e)}') 
        else:
            messages.error(request, 'Le nom de la catégorie ne peut pas être vide.') 
    return render(request, 'dashboard/categories/modifier_categorie.html', {'categorie': categorie})


def supprimer_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)  
    if request.method == 'POST':  
        categorie.delete()  
        messages.success(request, 'La catégorie a été supprimée avec succès !')  
        return redirect('affiche_categorie')  
    return render(request, 'dashboard/categories/supprimer_categorie.html', {'categorie': categorie})  



def affiche_categorie(request):
    categorie = Categorie.objects.all()
    context = {'categorie': categorie}
    return render(request, "dashboard/categories/affiche_categorie.html", context)



def Creer_article(request):
    categories = Categorie.objects.all()
    context = {
        'categories': categories,
    }
    if request.method == 'POST':
        form = Articles_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            Nom_article = form.cleaned_data["Nom_article"].lower()  # Convertir en minuscules
            if Article.objects.filter(Nom_article__iexact=Nom_article).exists():  # Utiliser iexact pour comparaison insensible à la casse
                messages.error(request, 'Un article avec le même nom existe déjà!')
            else:
                form.save()
                messages.success(request, 'Cet article a été créé avec succès!')
            return redirect('creer_article')
        else:
            context['form'] = form  # Ajouter le formulaire avec les erreurs au contexte
            return render(request, "dashboard/articles/creer_article.html", context)
    return render(request, "dashboard/articles/creer_article.html", context)


def Afficher_article(request):
    article = Article.objects.all()
    categorie = Categorie.objects.all()
    context = {"article":article, "categorie": categorie}
    return render(request,"dashboard/articles/afficher_article.html",context)

def Supprimer_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        messages.success(request, 'Cet article a été supprimé avec succes!')
        return redirect('afficher_article')
    return render(request, 'dashboard/articles/supprimer_article.html', {'article':article})



def Creer_service(request):
    if request.method =='POST':
        form = Services_form(request.POST, request.FILES)
        if form.is_valid():
            Nom_service = form.cleaned_data["Nom_service"].lower() 
            if Services.objects.filter(Nom_service__iexact = Nom_service).exists():
                messages.error(request, "Un services du même nom existe déjà!")
            else:
                form.save()
                messages.success(request, 'Ce services a été créé avec succès!')
            return redirect('creer_service')
    return render(request, "dashboard/services/creer_service.html")


def Afficher_services(request):
    services = Services.objects.all()
    context = {'services':services}
    return render(request, 'dashboard/services/afficher_services.html', context)

def Supprimer_service(request, id):
    services = get_object_or_404(Services, id=id)
    if request.method == 'POST':
        services.delete()
        messages.success(request, 'Ce service a été supprimé avec succes!')
        return redirect('afficher_services')
    return render(request, 'dashboard/services/supprimer_service.html', {'services':services})