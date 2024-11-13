from django.db import models

# Create your models here.
from django.db import models

class Role(models.Model):
    nom_role = models.CharField(max_length=100)  # Nom du rôle (ex: Président, Vice-Président)
    bureau = models.BooleanField(default=False)  # Si le rôle est un rôle de bureau
    com = models.BooleanField(default=False)  # Si le rôle est lié à la communication
    cyber = models.BooleanField(default=False)  # Si le rôle est lié à la cybersécurité

    def __str__(self):
        return self.nom_role

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    photo_profile = models.ImageField(upload_to='photos/', null=True,blank=True)  # Photo de profil
    tag_discord = models.CharField(max_length=100, unique=True)  # Tag Discord (unique)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)  # Rôle du membre (clé étrangère)
    lien_github = models.URLField(max_length=200, blank=True, null=True)  # Lien vers le GitHub
    lien_lk = models.URLField(max_length=200, blank=True, null=True)  # Lien vers le LinkedIn

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.role}"

class Techno(models.Model):
    nom = models.CharField(max_length=100)  # Nom de la technologie

    def __str__(self):
        return self.nom

class Projet(models.Model):
    nom_projet = models.CharField(max_length=200)  # Nom du projet
    description = models.TextField()  # Description du projet
    developpeur = models.ManyToManyField(Membre, blank=True)  # Développeurs du projet
    status = models.CharField(max_length=50, choices=[
        ('termine', 'Terminé'),
        ('en_cours', 'En Cours'),
        ('a_venir', 'À Venir'),
    ])  # Statut du projet
    lien_gitlab = models.URLField(max_length=200, blank=True, null=True)  # Lien vers la page GitLab
    image_projet = models.ImageField(upload_to='imgproj/',blank=True, null=True)  # Image du projet
    techno = models.ManyToManyField(Techno, blank=True)  # Technologies utilisées

    def __str__(self):
        return self.nom_projet

class Event(models.Model):
    nom_event = models.CharField(max_length=200)  # Nom de l'événement
    date_debut = models.DateField(blank=True, null=True)  # Date de début
    heure_debut = models.TimeField(blank=True, null=True)  # Heure de début
    date_fin = models.DateField(blank=True, null=True)  # Date de fin
    heure_fin = models.TimeField(blank=True, null=True)  # Heure de fin
    lieu = models.CharField(max_length=200)  # Lieu de l'événement
    description_courte = models.TextField()  # Courte description
    lien_page_event = models.URLField(max_length=200, blank=True, null=True)  # Lien vers la page de l'événement
    image_event = models.ImageField(upload_to='imgevent/')  # Image de l'événement

    def __str__(self):
        return self.nom_event

class Documentation(models.Model):
    nom_doc = models.CharField(max_length=200, unique=True)  # Nom de la documentation
    description = models.TextField()  # Description de la documentation
    lien_doc = models.URLField(max_length=200,blank=True, null=True)  # Lien vers la documentation
    image_doc = models.ImageField(upload_to='imgdoc/')  # Image de la documentation

    def __str__(self):
        return self.nom_doc
