from django.db import models

class Descuento(models.Model):
    valor = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.valor)

# Create your models here.
