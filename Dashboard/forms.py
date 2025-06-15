# Ce fichier permet de creer des formulaires basés sur des models crées dans le fichier models.
# Avec cette methode, on crée des formulaires directement liés aux models

from django import forms
from .models import Article, Services, Cat_categorie

class Articles_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class Services_form(forms.ModelForm):
    class Meta:   # la class interne meta est urilisée pour configurer les options du formulaire
        model = Services
        fields = '__all__'

class Cat_categorie_Form(forms.ModelForm):
    class Meta:
        model = Cat_categorie
        fields = '__all__'