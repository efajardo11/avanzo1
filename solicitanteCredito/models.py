from django.db import models

from pago.models import Pago

class Solicitante(models.Model):
    empresa = models.CharField(max_length=50)
    pago = models.ManyToManyField(Pago)

    def __str__(self):
        return '{}'.format(self.empresa)

# Create your models here.
