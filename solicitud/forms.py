from django import forms
from .models import Solicitud

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            'documento',
            'idSolicitud',
            'estado',
        ]

        labels = {
            'documento' : 'Documento',
            'idSolicitud' : 'IdSolicitud',
            'estado' : 'Estado',
        }