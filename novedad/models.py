from django.db import models

class Novedad(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.descripcion)
# Create your models here.
