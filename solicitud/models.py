from django.db import models

from documento.models import Documento

class Solicitud(models.Model):
    documento = models.ManyToManyField(Documento)
    idSolicitud = models.FloatField(null=True, blank=True, default=None)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.idSolicitud, self.estado)

# Create your models here.
