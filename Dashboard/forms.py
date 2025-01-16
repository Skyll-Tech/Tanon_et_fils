from django import forms
from .models import Article

class Articles_form(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'