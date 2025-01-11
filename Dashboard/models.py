from django.db import models

# Create your models here.
class Categorie(models.Model):
    Nom_categorie = models.CharField(max_length=25, unique=True)
    Nb_article = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.Nom_categorie}"