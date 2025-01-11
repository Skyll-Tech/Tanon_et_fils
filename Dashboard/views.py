from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages 
from django.db import IntegrityError
from .models import Categorie


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
        
    return render(request,"dashboard/creer_categorie.html")



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
    return render(request, 'dashboard/modifier_categorie.html', {'categorie': categorie})


def supprimer_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)  
    if request.method == 'POST':  
        categorie.delete()  
        messages.success(request, 'La catégorie a été supprimée avec succès !')  
        return redirect('affiche_categorie')  
    return render(request, 'dashboard/supprimer_categorie.html', {'categorie': categorie})  



def affiche_categorie(request):
    categorie = Categorie.objects.all()
    context = {'categorie': categorie}
    return render(request, "dashboard/affiche_categorie.html", context)

def Creer_article(request):
    categorie = Categorie.objects.all()
    context = {'categorie':categorie}
    return render(request,"dashboard/creer_article.html",context)