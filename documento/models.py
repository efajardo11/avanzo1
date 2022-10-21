from django.db import models

class Documento(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.tipo)

# Create your models here.
