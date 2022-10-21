from django.db import models

class Adiministrativo(models.Model):
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.tipo)
# Create your models here.
