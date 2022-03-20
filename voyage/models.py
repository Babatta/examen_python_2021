from django.db import models
from django import forms
from destination.models import Destination

# Create your models here.
class Voyage(models.Model):
    id_destination=models.ForeignKey(Destination,null=True,on_delete=models.SET_NULL)
    nomvoyage=models.CharField(max_length=100,null=True)
    duree=models.IntegerField(null=True)
    photo=models.ImageField(upload_to = 'pics/',default = 'pics/voy.png')
    prix=models.FloatField(null=True)
    date_creation=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.nomvoyage





