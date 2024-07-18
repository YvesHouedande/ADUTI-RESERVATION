from django.db import models

class Reservation(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    annee_sortie = models.DateField()
    diner_precedent = models.CharField(max_length=3, choices=[('oui', 'Oui'), ('non', 'Non')])

    def __str__(self):
        return f"{self.nom} {self.prenom}"
