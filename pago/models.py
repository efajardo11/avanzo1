from django.db import models
from descuento.models import Descuento
from novedad.models import Novedad

class Pago(models.Model):
    valor = models.IntegerField(null=True, blank=True, default=None)
    descuento = models.ManyToManyField(Descuento)
    descripcion = models.ManyToManyField(Novedad)

    def __str__(self):
        return '{}'.format(self.valor)

# Create your models here.
