from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Role)  # Enregistrement du modèle Role
admin.site.register(Membre)  # Enregistrement du modèle Membre
admin.site.register(Projet)  # Enregistrement du modèle Projets
admin.site.register(Event)  # Enregistrement du modèle Events
admin.site.register(Documentation)  # Enregistrement du modèle Documentation
admin.site.register(Techno)  # Enregistrement du modèle Techno

