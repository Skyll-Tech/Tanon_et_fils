from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Categorie(models.Model):
    Nom_categorie = models.CharField(max_length=25, unique=True)
    Nb_article = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.Nom_categorie}"
    

class Article(models.Model):
    
    DISPONIBLE = 'disponible'
    NON_DISPONIBLE = 'non disponible'
    CHOIX_STATUT = [(DISPONIBLE,'Disponible'), (NON_DISPONIBLE, 'Non disponible'),]  # liste de tuple pour le choix du statut d'un article
    
    
    Nom_article = models.CharField(max_length=50, unique=True)
    Categorie_atc = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    Quantite_atc = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null = True)
    Prix_atc = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Description_atc = models.TextField(blank=True, null = True)
    Image_atc = models.ImageField(upload_to='images_articles/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.Nom_article}"