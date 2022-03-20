from django.db import models
from voyage.models import Voyage
# Create your models here.
class Excursion(models.Model):
    nom=models.CharField(max_length=100,null=True)
    photoexcursion = models.ImageField(upload_to='pics',default=False)
    optionnelle=models.BooleanField(default=False)
    voyage = models.ManyToManyField(Voyage)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.nom