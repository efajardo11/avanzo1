from django.db import models
from solicitud.models import Solicitud
from documento.models import Documento

class Usuario(models.Model):
    numeroDocumento = models.IntegerField(null=True, blank=True, default=None)
    ##nombre = models.CharField(max_lenght=50)
    solicitud = models.ManyToManyField(Solicitud)
    tipoDocumento = models.ManyToManyField(Documento)

    def __str__(self):
        return '{}'.format(self.nombre, self.numeroDocumento)
