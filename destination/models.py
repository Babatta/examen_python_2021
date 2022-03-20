from django.db import models

# Create your models here.
class Destination(models.Model):
        pays=models.CharField(max_length=50,null=True)
        image=models.ImageField(upload_to='pics')
        date_creation = models.DateTimeField(auto_now_add=True, null=True)
        def __str__(self):
                return self.pays