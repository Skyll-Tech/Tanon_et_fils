from django.contrib import admin
from .models import Categorie, Article, Services, Cat_categorie
# Register your models here.

admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(Services)
admin.site.register(Cat_categorie)