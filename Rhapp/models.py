from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Superviseur(models.Model):
    nom = models.CharField(max_length=200)
    Prenom = models.CharField(max_length=200)
    departement = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __unicode__(self):
        return f"Superviseur: {self.first_name} {self.last_name}"


class Personne(models.Model):
        
        nom =models.CharField(max_length=100)
        prenom=models.CharField(max_length=100)
        departement =models.CharField(max_length=100)
        active = models.BooleanField(default=True)
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        Superviseur = models.ForeignKey(Superviseur, on_delete=models.CASCADE)
        date_of_formation = models.DateField()
        
        def __unicode__(self):
            return f"{self.first_name} {self.last_name}"