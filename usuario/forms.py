from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'numeroDocumento',
            'solicitud',
            'tipoDocumento',
            #'nombre',
        ]

        labels = {
            'numeroDocumento' : 'NumeroDocumento',
            'solicitud' : 'Solicitud',
            'tipoDocumento' : 'TipoDocumento',
            #'nombre' : 'Nombre',
        }