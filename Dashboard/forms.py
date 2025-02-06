from django import forms
from .models import Article, Services

class Articles_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class Services_form(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'